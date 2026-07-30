# Digital Logic
comparator
	compares two voltages
		asserted (high) vs deasserted (low)
combinational (logic only) vs sequential (logic + state)
	truth tables ($n$ inputs, $2^n$ entries)
logic standards
1. transistor transistor logic (TTL)
2. emitter coupled logic (ECL)
3. NIM logic
4. Complementary Metal Oxide Semiconductor (CMOS)
	basis of modern digital computing
## Basic Logic Operations
see [Logical Operators](logic-proofs.md#logical-operators)
notation
	$\cdot$ (and)
	$+$ (or)
	$\bar{~}$ (not)
	$\oplus$ (xor, try not to use)
sum of products form
	product terms (aka minterms)
	programmable logic array
	karnaugh maps, minimization
## Combinational Logic
decoders
	$n$ bit input, $2^n$ bit output
	encoder does opposite
multiplexor (mux)
	$n$ bit selector value, $2^n$ inputs, $1$ output
	demux does opposite
read only memory (ROM)
	sometimes programmable
bus: collection of dat lines
arithmetic logic unit (ALU)
	mux with inputs hooked to logic/arithmetic gates
	ripple carry: hook adders to each other
	carry lookahead: generate and propagate ($c_n = g_{n-1} + (p_{n-1} \cdot c_{n-1})$)
### Hardware Description Languages
verilog and VHDL
behavioral and structural specs
wire vs reg
blocking (completes before next) vs nonblocking (only after right side evaluated)
## Sequential Logic
clocks
	rising/falling edge
	edge vs level trigger
	edge triggering: become active at positive or negative edge
finite state machine
	set of states and function mapping state to next state
	microcode
	moore (state nd input) vs mealy (state, more stable)
### Feedback
flip flops: output = stored, changes only with clock edge
	D flip flop: 1 data input
		other types: SR, JK, T
	set up time (minimum before) and hold time (minimum after)
latch: output = stored, changes only when clock asserted
	active high: SET/RESET when control input goes to TRUE
	active low: SET/RESET when control input goes to FALSE
memory elements
	static vs dynamic RAM (lots of muxing)
open collector logic
	internal of TTL
	open collector busses
FPGA (field programmable gate array) vs ASIC (application specific integrated circuits)