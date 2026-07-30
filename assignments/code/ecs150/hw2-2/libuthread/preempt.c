#include <signal.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#include "private.h"
#include "uthread.h"

/*
 * Frequency of preemption
 * 100Hz is 100 times per second
 */
#define HZ 100
#define MICRO 1000000

static struct sigaction prev_action;
static struct itimerval prev_timer;
static bool preempt_enabled = false;

static void alarm_handler(int sig)
{
    (void)sig;
    uthread_yield();
}

void preempt_disable(void)
{
    if (preempt_enabled) {
        sigset_t block_set;
        sigemptyset(&block_set);
        sigaddset(&block_set, SIGVTALRM);
        sigprocmask(SIG_BLOCK, &block_set, NULL);
    }
}

void preempt_enable(void)
{
    if (preempt_enabled) {
        sigset_t unblock_set;
        sigemptyset(&unblock_set);
        sigaddset(&unblock_set, SIGVTALRM);
        sigprocmask(SIG_UNBLOCK, &unblock_set, NULL);
    }
}

void preempt_start(bool preempt)
{
    if (!preempt) {
        preempt_enabled = false;
        return;
    }

    /* install signal handler */
    struct sigaction action;
    action.sa_handler = alarm_handler;
    sigemptyset(&action.sa_mask);
    action.sa_flags = 0;

    if (sigaction(SIGVTALRM, &action, &prev_action) == -1) {
        perror("sigaction");
        exit(1);
    }

    /* timer that fires at 100 Hz */
    struct itimerval timer;
    timer.it_value.tv_sec = 0;
    timer.it_value.tv_usec = MICRO / HZ;
    timer.it_interval.tv_sec = 0;
    timer.it_interval.tv_usec = MICRO / HZ;

    if (setitimer(ITIMER_VIRTUAL, &timer, &prev_timer) == -1) {
        perror("setitimer");
        exit(1);
    }

    preempt_enabled = true;
}

void preempt_stop(void)
{
    if (preempt_enabled) {
        /* restore previous timer */
        if (setitimer(ITIMER_VIRTUAL, &prev_timer, NULL) == -1) {
            perror("setitimer");
            exit(1);
        }
        /* restore previous signal action */
        if (sigaction(SIGVTALRM, &prev_action, NULL) == -1) {
            perror("sigaction");
            exit(1);
        }
        preempt_enabled = false;
    }
}
