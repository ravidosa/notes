#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include <queue.h>

#define TEST_ASSERT(assert)                                                    \
    do {                                                                       \
        printf("ASSERT: " #assert " ... ");                                    \
        if (assert) {                                                          \
            printf("PASS\n");                                                  \
        } else {                                                               \
            printf("FAIL\n");                                                  \
            exit(1);                                                           \
        }                                                                      \
    } while (0)

/* Create */
void test_create(void)
{
    queue_t q;

    fprintf(stderr, "*** TEST create ***\n");

    TEST_ASSERT((q = queue_create()) != NULL);
    queue_destroy(q);
}

/* Enqueue/Dequeue simple */
void test_queue_simple(void)
{
    int data = 3, *ptr;
    queue_t q;

    fprintf(stderr, "*** TEST queue_simple ***\n");

    q = queue_create();
    queue_enqueue(q, &data);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    queue_destroy(q);
}

void test_destroy(void)
{
    int data = 3, *ptr;
    queue_t q;

    fprintf(stderr, "*** TEST destroy ***\n");
    TEST_ASSERT(queue_destroy(NULL) == -1);

    q = queue_create();
    queue_enqueue(q, &data);
    TEST_ASSERT(queue_destroy(q) == -1);

    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(queue_destroy(q) == 0);
}

void test_enqueue(void)
{
    int data = 3, *ptr;
    int dataa = 4;
    queue_t q;

    fprintf(stderr, "*** TEST enqueue ***\n");
    q = queue_create();
    TEST_ASSERT(queue_enqueue(NULL, &data) == -1);
    TEST_ASSERT(queue_enqueue(q, NULL) == -1);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataa);
    queue_destroy(q);
}

void test_dequeue(void)
{
    int data = 3, *ptr;
    queue_t q;

    fprintf(stderr, "*** TEST dequeue ***\n");
    q = queue_create();
    queue_enqueue(q, &data);
    TEST_ASSERT(queue_dequeue(NULL, (void **)&ptr) == -1);
    TEST_ASSERT(queue_dequeue(q, NULL) == -1);

    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    TEST_ASSERT(queue_dequeue(q, (void **)&ptr) == -1);
    queue_destroy(q);
}

void test_enqueue_dequeue(void)
{
    int data = 3, *ptr;
    int dataa = 4;
    int dataaa = 5;
    queue_t q;

    fprintf(stderr, "*** TEST enqueue_dequeue ***\n");
    q = queue_create();

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_enqueue(q, &dataaa);
    TEST_ASSERT(queue_length(q) == 3);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    TEST_ASSERT(queue_length(q) == 2);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataa);
    TEST_ASSERT(queue_length(q) == 1);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataaa);
    TEST_ASSERT(queue_length(q) == 0);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    queue_enqueue(q, &dataaa);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataa);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataaa);
    queue_destroy(q);
}

void test_delete(void)
{
    int data = 3, *ptr;
    int dataa = 4;
    int dataaa = 5;
    queue_t q;

    fprintf(stderr, "*** TEST delete ***\n");
    q = queue_create();
    queue_enqueue(q, &data);
    TEST_ASSERT(queue_delete(NULL, &data) == -1);
    TEST_ASSERT(queue_delete(q, NULL) == -1);

    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(queue_delete(q, &data) == -1);

    queue_enqueue(q, &data);
    TEST_ASSERT(queue_delete(q, &dataa) == -1);
    TEST_ASSERT(queue_delete(q, &data) == 0);
    TEST_ASSERT(queue_length(q) == 0);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_enqueue(q, &dataaa);
    TEST_ASSERT(queue_delete(q, &dataa) == 0);
    TEST_ASSERT(queue_length(q) == 2);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataaa);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_enqueue(q, &dataaa);
    TEST_ASSERT(queue_delete(q, &data) == 0);
    TEST_ASSERT(queue_length(q) == 2);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataa);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataaa);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_enqueue(q, &dataaa);
    TEST_ASSERT(queue_delete(q, &dataaa) == 0);
    TEST_ASSERT(queue_length(q) == 2);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &data);
    queue_dequeue(q, (void **)&ptr);
    TEST_ASSERT(ptr == &dataa);
    queue_destroy(q);
}

static int iterator_count = 0;

static void iterator_counter(queue_t q, void *data)
{
    (void)q;
    (void)data;
    iterator_count++;
}

static int iterator_sum = 0;

static void iterator_summer(queue_t q, void *data)
{
    (void)q;
    int *num = (int *)data;
    iterator_sum += *num;
}

static void iterator_deleter(queue_t q, void *data)
{
    int *num = (int *)data;
    if (*num == 4) {
        queue_delete(q, data);
    }
}

void test_iterate(void)
{
    int data = 3, *ptr;
    int dataa = 4;
    int dataaa = 5;
    queue_t q;

    fprintf(stderr, "*** TEST iterate ***\n");
    q = queue_create();
    TEST_ASSERT(queue_iterate(NULL, iterator_counter) == -1);
    TEST_ASSERT(queue_iterate(q, NULL) == -1);

    iterator_count = 0;
    TEST_ASSERT(queue_iterate(q, iterator_counter) == 0);
    TEST_ASSERT(iterator_count == 0);

    queue_enqueue(q, &data);
    queue_enqueue(q, &dataa);
    queue_enqueue(q, &dataaa);
    iterator_count = 0;
    TEST_ASSERT(queue_iterate(q, iterator_counter) == 0);
    TEST_ASSERT(iterator_count == 3);

    iterator_sum = 0;
    TEST_ASSERT(queue_iterate(q, iterator_summer) == 0);
    TEST_ASSERT(iterator_sum == 12);

    TEST_ASSERT(queue_iterate(q, iterator_deleter) == 0);
    TEST_ASSERT(queue_length(q) == 2);
    queue_dequeue(q, (void **)&ptr);
    queue_dequeue(q, (void **)&ptr);
    queue_destroy(q);
}

void test_length(void)
{
    int data = 3, *ptr;
    int dataa = 4;
    int dataaa = 5;
    queue_t q;

    fprintf(stderr, "*** TEST length ***\n");
    q = queue_create();
    TEST_ASSERT(queue_length(NULL) == -1);
    TEST_ASSERT(queue_length(q) == 0);

    queue_enqueue(q, &data);
    TEST_ASSERT(queue_length(q) == 1);
    queue_enqueue(q, &dataa);
    TEST_ASSERT(queue_length(q) == 2);
    queue_enqueue(q, &dataaa);
    TEST_ASSERT(queue_length(q) == 3);
    queue_dequeue(q, (void **)&ptr);
    queue_dequeue(q, (void **)&ptr);
    queue_dequeue(q, (void **)&ptr);
    queue_destroy(q);
}

int main(void)
{
    test_create();
    test_queue_simple();
    test_destroy();
    test_enqueue();
    test_dequeue();
    test_enqueue_dequeue();
    test_delete();
    test_iterate();
    test_length();

    return 0;
}
