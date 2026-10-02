/*
 * Preemption test
 * Tests the creation of a thread which never voluntarily yields, and its
 * interruption to allow other threads to run
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include <uthread.h>

static volatile int arr[2];

void thread2(void *arg)
{
    (void)arg;
    arr[1] = 1;
    printf("thread2\n");
}

void thread1(void *arg)
{
    (void)arg;
    arr[0] = 1;
    printf("thread1 (waiting for preemption)\n");

    uthread_create(thread2, NULL);

    while (arr[1] == 0) {
        /* needs preemption for interrupt */
    }

    printf("thread1 (preempted by thread2)\n");
}

int main(void)
{
    if (uthread_run(true, thread1, NULL) == -1) {
        fprintf(stderr, "uthread_run failed\n");
        return 1;
    }

    if (arr[0] && arr[1]) {
        printf("both threads ran\n");
        return 0;
    } else {

        fprintf(stderr, "at least one thread failed\n");
        return 1;
    }
}