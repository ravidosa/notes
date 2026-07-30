# Processor
datapath elements (hold data in processor)
	program counter (PC): contain address of instruction
	instructor read (IR): decode instruction
	register file: store registers
	handling immediates/jump: sign extend
	arithmetic logic unit (ALU): see [digital logic](digital-logic.md)
	memory
single cycle vs multicycle
	CPI = instruction count x cycles per instruction x cycle time
	single cycle is inefficient (same clock cycle for everything)
	multicycle uses pipelining
		stages should be similar length (combine or split stages)
		pipeline hazards (prevent these, cause stalls)
			structural hazard: hardware does not support instructions
			data hazard: data needed not yet available
				forwarding
				hazard detection, add nops
			control hazard: incorrect instruction fetched
				branch prediction
					dynamic branch prediction (branch predictor buffer)
		exceptions/interrupts
			vectored interrupt: address of transfer determined by cause of exception
		cost of speculation
			very long instruction word (VLIW)
				static
				loop unrolling (needs register renamic)
			superscalar
				dynamic
				reorder buffer for out-of-order execution
	pipeline
		instruction fetch
		instruction decode and register fetch
		execution/memory address computation/branch completion
		memory access/ALU instruction
		memory read (write back)
	represent as finite state machine