#include <assert.h>
#include <signal.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#include "private.h"
#include "queue.h"
#include "uthread.h"

enum thread_state { RUNNING, READY, BLOCKED, TERMINATED };

struct uthread_tcb {
    enum thread_state state;
    uthread_ctx_t ctx;
    void *stack;
};

static queue_t available_threads;
static struct uthread_tcb *current_thread;
static struct uthread_tcb *idle_thread;

static void next_available_thread(void)
{
    struct uthread_tcb *next_thread;

    /* available thread in queue */
    if (queue_dequeue(available_threads, (void **)&next_thread) == 0) {
        /* store old thread in prev, new thread in current and update state */
        struct uthread_tcb *prev_thread = current_thread;
        current_thread = next_thread;
        current_thread->state = RUNNING;
        /* switch execution contexts */
        uthread_ctx_switch(&(prev_thread->ctx), &(current_thread->ctx));
    }
}

struct uthread_tcb *uthread_current(void) { return current_thread; }

void uthread_yield(void)
{
    preempt_disable();

    /* return current thread to queue if still running */
    if (current_thread->state == RUNNING) {
        current_thread->state = READY;
        queue_enqueue(available_threads, current_thread);
    }
    next_available_thread();
    preempt_enable();
}

void uthread_exit(void)
{
    preempt_disable();
    current_thread->state = TERMINATED;

    /* free up resources */
    if (current_thread != idle_thread) {
        uthread_ctx_destroy_stack(current_thread->stack);
        free(current_thread);
    }
    next_available_thread();
}

int uthread_create(uthread_func_t func, void *arg)
{
    /* allocate tcb */
    struct uthread_tcb *new_thread = malloc(sizeof(struct uthread_tcb));
    if (new_thread == NULL) {
        return -1;
    }

    /* allocate stack */
    new_thread->stack = uthread_ctx_alloc_stack();
    if (new_thread->stack == NULL) {
        free(new_thread);
        return -1;
    }

    /* initialize context */
    if (uthread_ctx_init(&(new_thread->ctx), new_thread->stack, func, arg) ==
        -1) {
        uthread_ctx_destroy_stack(new_thread->stack);
        free(new_thread);
        return -1;
    }

    /* set state to ready, add thread to queue */
    new_thread->state = READY;
    preempt_disable();
    if (queue_enqueue(available_threads, new_thread) == -1) {
        uthread_ctx_destroy_stack(new_thread->stack);
        free(new_thread);
        return -1;
    }

    preempt_enable();
    return 0;
}

int uthread_run(bool preempt, uthread_func_t func, void *arg)
{
    available_threads = queue_create();
    if (available_threads == NULL) {
        return -1;
    }

    /* create idle thread */
    idle_thread = malloc(sizeof(struct uthread_tcb));
    if (idle_thread == NULL) {
        queue_destroy(available_threads);
        return -1;
    }

    idle_thread->stack = NULL;
    idle_thread->state = RUNNING;
    current_thread = idle_thread;

    /* create initial thread */
    if (uthread_create(func, arg) == -1) {
        free(idle_thread);
        queue_destroy(available_threads);
        return -1;
    }

    preempt_start(preempt);

    /* infinite loop of yielding while available threads*/
    while (queue_length(available_threads) > 0) {
        uthread_yield();
    }

    free(idle_thread);
    queue_destroy(available_threads);
    if (preempt) {
        preempt_stop();
    }
    return 0;
}

void uthread_block(void)
{
    preempt_disable();
    current_thread->state = BLOCKED;
    next_available_thread();
    preempt_enable();
}

void uthread_unblock(struct uthread_tcb *uthread)
{
    preempt_disable();
    if (uthread->state == BLOCKED) {
        uthread->state = READY;
        queue_enqueue(available_threads, uthread);
    }
    preempt_enable();
}
