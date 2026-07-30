#include "scheduler.h"
#include <stdlib.h>
#include <ucontext.h>

static ucontext_t main_ctx;
static ucontext_t task_ctx[TASK_COUNT_MAX];
static char *task_stack[TASK_COUNT_MAX];

void free_stack(int low, int high)
{
    for (int j = low; j < high; j++) {
        free(task_stack[j]);
    }
}

int scheduler_run(void (*task_func)(int), int task_cnt, const int *task_sched)
{
    /* invalid args */
    if (!task_func || !task_sched || task_cnt < 1 ||
        task_cnt > TASK_COUNT_MAX) {
        return -1;
    }

    for (int i = 0; i < task_cnt; i++) {
        /* getcontext failure */
        if (getcontext(&task_ctx[i]) == -1) {
            free_stack(0, i);
            return -1;
        }
        task_stack[i] = malloc(STACK_SIZE);
        /* malloc failure */
        if (!task_stack[i]) {
            free_stack(0, i);
            return -1;
        }
        task_ctx[i].uc_stack.ss_sp = task_stack[i];
        task_ctx[i].uc_stack.ss_size = STACK_SIZE;
        makecontext(&task_ctx[i], (void (*)(void))task_func, 1, i);
    }

    int sched_idx = 0;
    while (1) {
        int next_task = task_sched[sched_idx];

        /* flag to end scheduling */
        if (next_task == -1) {
            break;
        }

        /* invalid task ID */
        if (next_task < 0 || next_task >= task_cnt) {
            free_stack(0, task_cnt);
            return -1;
        }

        sched_idx++;
        swapcontext(&main_ctx, &task_ctx[next_task]);
    }
    free_stack(0, task_cnt);
    return 0;
}

void scheduler_yield(int task_id)
{
    swapcontext(&task_ctx[task_id], &main_ctx);
}
