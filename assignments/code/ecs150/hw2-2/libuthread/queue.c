#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include "queue.h"

/*
 * doubly linked list for O(1) operations
 * https://www.geeksforgeeks.org/c/doubly-linked-list-in-c/
 */

struct node {
    void *data;
    struct node *next;
    struct node *prev;
};

struct queue {
    struct node *head;
    struct node *tail;
    int length;
};

queue_t queue_create(void)
{
    queue_t queue = (queue_t)malloc(sizeof(struct queue));

    if (queue == NULL) {
        return NULL;
    }

    queue->head = NULL;
    queue->tail = NULL;
    queue->length = 0;
    return queue;
}

int queue_destroy(queue_t queue)
{
    if (queue == NULL || queue->length != 0) {
        return -1;
    }

    free(queue);
    return 0;
}

int queue_enqueue(queue_t queue, void *data)
{
    if (queue == NULL || data == NULL) {
        return -1;
    }

    struct node *enq = (struct node *)malloc(sizeof(struct node));
    if (enq == NULL) {
        return -1;
    }

    enq->data = data;
    enq->next = NULL;

    if (queue->length == 0) {
        queue->head = enq;
        queue->tail = enq;
        enq->prev = NULL;
    } else {
        queue->tail->next = enq;
        enq->prev = queue->tail;
        queue->tail = enq;
    }

    queue->length++;
    return 0;
}

int queue_dequeue(queue_t queue, void **data)
{
    if (queue == NULL || data == NULL) {
        return -1;
    }

    if (queue->length == 0) {
        return -1;
    }

    struct node *deq = queue->head;
    *data = deq->data;
    queue->head = deq->next;

    if (queue->head == NULL) {
        queue->tail = NULL;
    } else {
        queue->head->prev = NULL;
    }

    queue->length--;
    free(deq);
    return 0;
}

int queue_delete(queue_t queue, void *data)
{
    if (queue == NULL || data == NULL) {
        return -1;
    }

    struct node *curr = queue->head;

    while (curr != NULL) {
        if (curr->data == data) {
            if (curr == queue->head) {
                queue->head = curr->next;
                if (queue->head == NULL) {
                    queue->tail = NULL;
                } else {
                    queue->head->prev = NULL;
                }
            } else {
                curr->prev->next = curr->next;
                if (curr == queue->tail) {
                    queue->tail = curr->prev;
                } else {
                    curr->next->prev = curr->prev;
                }
            }

            queue->length--;
            free(curr);
            return 0;
        }

        curr = curr->next;
    }

    return -1;
}

int queue_iterate(queue_t queue, queue_func_t func)
{
    if (queue == NULL || func == NULL) {
        return -1;
    }

    struct node *curr = queue->head;

    while (curr != NULL) {
        struct node *next = curr->next;
        func(queue, curr->data);
        curr = next;
    }

    return 0;
}

int queue_length(queue_t queue)
{
    if (queue == NULL) {
        return -1;
    }

    return queue->length;
}
