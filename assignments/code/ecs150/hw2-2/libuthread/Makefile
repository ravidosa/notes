# Target library
lib := libuthread.a

all: $(lib)

objs := queue.o uthread.o context.o preempt.o sem.o

CC := gcc
CFLAGS := -Wall -Wextra -Werror -MMD
CFLAGS += -g
AR := ar
ARFLAGS := rcs

deps := $(patsubst %.o,%.d,$(objs))
-include $(deps)

$(lib): $(objs)
	$(AR) $(ARFLAGS) $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(lib) $(objs) $(deps)