#include <stddef.h>
#include <stdlib.h>

#include "private.h"
#include "queue.h"
#include "sem.h"

struct semaphore {
    size_t count;
    queue_t blocked_threads;
};

sem_t sem_create(size_t count)
{
    /* allocate semaphore */
    struct semaphore *new_semaphore = malloc(sizeof(struct semaphore));
    if (new_semaphore == NULL) {
        return NULL;
    }

    /* initialize count, blocked threads*/
    new_semaphore->count = count;
    new_semaphore->blocked_threads = queue_create();
    if (new_semaphore->blocked_threads == NULL) {
        free(new_semaphore);
        return NULL;
    }
    return new_semaphore;
}

int sem_destroy(sem_t sem)
{
    if (sem == NULL) {
        return -1;
    }

    if (queue_length(sem->blocked_threads) > 0) {
        return -1;
    }

    queue_destroy(sem->blocked_threads);
    free(sem);
    return 0;
}

int sem_down(sem_t sem)
{
    if (sem == NULL) {
        return -1;
    }

    preempt_disable();
    if (sem->count == 0) {
        struct uthread_tcb *current_thread = uthread_current();
        if (queue_enqueue(sem->blocked_threads, current_thread) == -1) {
            preempt_enable();
            return -1;
        }
        preempt_enable();

        /* loop until sem_up, then dequeue */
        while (sem->count == 0) {
            uthread_block();
        }

        preempt_disable();
        void *unblocked;
        queue_dequeue(sem->blocked_threads, &unblocked);
    }

    sem->count--;
    preempt_enable();
    return 0;
}

static struct uthread_tcb *peek_thread;

static void peek_blocked_threads(queue_t queue, void *data)
{
    (void)queue;

    if (peek_thread == NULL) {
        peek_thread = (struct uthread_tcb *)data;
    }
}

int sem_up(sem_t sem)
{
    if (sem == NULL) {
        return -1;
    }

    /* release resource */
    preempt_disable();
    sem->count++;

    if (queue_length(sem->blocked_threads) > 0) {
        /* only dequeue once it gets the resource in sem_down to avoid
         * starvation */
        peek_thread = NULL;
        queue_iterate(sem->blocked_threads, peek_blocked_threads);

        if (peek_thread != NULL) {
            uthread_unblock(peek_thread);
        }
    }

    preempt_enable();
    return 0;
}
