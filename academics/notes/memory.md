# Memory
principle of locality
	temporal and spatial
		lest recently used (LRU)
memory hierarchy
	multiple levels of memory with different size, speed
	AMAT = hit time + miss rate x miss penalty
	handling cache misses
		compulsory: first access miss
		capacity: cache cannot contain all blocks needed
		conflict: multiple blocks in one set
	cache coherence
	writing to cache
		write back (dirty bit) vs write through
static vs dynamic RAM
	SRAM doesn't need to refresh, minimal power
	DRAM nonpersistent, much better access time
		synchronous DRAM
disk memory
	seek time, rotational latency
cache mappings
	direct: block can go in only one location
	fully associative: block can be placed anywhere in cache
	set associative: fixed number of locations for block (in the middle of two above)
	multilevel cache
virtual memory
	main memory as cache for secondary storage
	translate address pace to physical addresses in main memory
		page fault (handle with kernel and syscall, handler)
	address mapping with translation lookaside buffer (TLB)