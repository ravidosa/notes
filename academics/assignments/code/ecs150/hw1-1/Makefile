# based on assignment 0 makefile
TARGET := sshell

# Compiler and flags
CC := gcc
CFLAGS_COMMON  := -Wall -Wextra -Werror
CFLAGS_DEBUG   := $(CFLAGS_COMMON) -g
CFLAGS_RELEASE := $(CFLAGS_COMMON) -O2

all: release

release: CFLAGS := $(CFLAGS_RELEASE)
release: $(TARGET)

debug: CFLAGS := $(CFLAGS_DEBUG)
debug: $(TARGET)

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)

.PHONY: all release debug clean
