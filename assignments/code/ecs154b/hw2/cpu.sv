// ============================================================================
// MODULE: Memory (Single-Port RAM)
// ============================================================================
module memory_module (
    input  logic       clk,
    input  logic [7:0] addr,
    input  logic       write_en,
    input  logic [7:0] data_in,
    output logic [7:0] data_out
);
    logic [7:0] mem [0:255];

    initial begin
        for (int i = 0; i < 256; i++) mem[i] = 0;
    end

    assign data_out = mem[addr];

    always_ff @(posedge clk) begin
        if (write_en)
            mem[addr] <= data_in;
    end
endmodule


// ============================================================================
// MODULE: ALU
// ============================================================================
module alu (
    input  logic [7:0] a,
    input  logic [7:0] b,
    input  logic [1:0] func,
    output logic [7:0] result,
    output logic       zero
);
    always_comb begin
        case (func)
            2'b11:   result = a + b;
            2'b10:   result = a - b;
            2'b01:   result = a * b;
            2'b00:   result = ~(a & b);
            default: result = 8'h00;
        endcase
    end
    assign zero = (result == 8'h00);
endmodule


// ============================================================================
// MODULE: Control Unit
// ============================================================================
module control_unit (
    input  logic       clk,
    input  logic       reset,
    input  logic [3:0] opcode,
    input  logic       alu_zero,

    output logic       halted,

    output logic       ir_load,
    output logic       pc_inc,
    output logic       pc_branch,
    output logic       pc_jump,
    output logic       reg_write,
    output logic       mem_write,
    output logic       mem_sel,
    output logic [1:0] alu_src,
    output logic [1:0] alu_func,
    output logic       latch_wb,
    output logic       latch_is_mem
);

    typedef enum logic [2:0] {
        FETCH     = 3'd0,
        DECODE    = 3'd1,
        EXECUTE   = 3'd2,
        MEMORY    = 3'd3,
        WRITEBACK = 3'd4,
        HALT      = 3'd5
    } state_t;

    state_t state, next_state;

    logic [3:0] op_reg;
    logic       zero_reg;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            state    <= FETCH;
            op_reg   <= 4'b1110;
            zero_reg <= 1'b0;
        end else begin
            state <= next_state;
            if (state == DECODE) begin
                op_reg   <= opcode;
                zero_reg <= alu_zero;
            end
        end
    end

    always_comb begin
        case (state)
            FETCH:     next_state = DECODE;
            DECODE:    next_state = EXECUTE;
            EXECUTE: begin
                if (op_reg == 4'b0010 || op_reg == 4'b0110)
                    next_state = MEMORY;
                else
                    next_state = WRITEBACK;
            end
            MEMORY:    next_state = WRITEBACK;
            WRITEBACK: begin
                if (op_reg == 4'b1111)
                    next_state = HALT;
                else
                    next_state = FETCH;
            end
            HALT:      next_state = HALT;
            default:   next_state = FETCH;
        endcase
    end

    always_comb begin
        ir_load      = 1'b0;
        pc_inc       = 1'b0;
        pc_branch    = 1'b0;
        pc_jump      = 1'b0;
        reg_write    = 1'b0;
        mem_write    = 1'b0;
        mem_sel      = 1'b0;
        alu_src      = 2'b00;
        alu_func     = 2'b11;
        latch_wb     = 1'b0;
        latch_is_mem = 1'b0;

        case (state)
            FETCH: begin
                mem_sel = 1'b0;
                ir_load = 1'b1;
                pc_inc  = 1'b1;
            end
            DECODE: begin
                alu_func = 2'b10;
                alu_src  = 2'b00;
            end
            EXECUTE: begin
                case (op_reg)
                    4'b0000, 4'b0001, 4'b0011, 4'b0100, 4'b0101: begin
                        latch_wb = 1'b1;
                        latch_is_mem = 1'b0;
                    end
                    4'b0010, 4'b0110, 4'b0111: begin
                        mem_sel = 1'b1;
                    end
                    default: ;
                endcase
                case (op_reg)
                    4'b0000: begin
                        alu_func = 2'b00;
                        alu_src = 2'b00;
                    end
                    4'b0001: begin
                        alu_func = 2'b11;
                        alu_src = 2'b00;
                    end
                    4'b0011: begin
                        alu_func = 2'b11;
                        alu_src = 2'b10;
                    end
                    4'b0100: begin
                        alu_func = 2'b10;
                        alu_src = 2'b00;
                    end
                    4'b0101: begin
                        alu_func = 2'b01;
                        alu_src = 2'b00;
                    end
                    4'b0111: begin
                        mem_write = 1'b1;
                    end
                    4'b1000: begin
                        if (zero_reg) pc_branch = 1'b1;
                    end
                    4'b1001: begin
                        pc_jump = 1'b1;
                    end
                    default: ;
                endcase
            end
            MEMORY: begin
                mem_sel = 1'b1;
                case (op_reg)
                    4'b0010: begin
                        alu_func = 2'b11;
                        alu_src = 2'b01;
                        latch_wb = 1'b1;
                        latch_is_mem = 1'b0;
                    end
                    4'b0110: begin
                        latch_wb = 1'b1;
                        latch_is_mem = 1'b1;
                    end
                    default: ;
                endcase
            end
            WRITEBACK: begin
                case (op_reg)
                    4'b0000, 4'b0001, 4'b0010,
                    4'b0011, 4'b0100, 4'b0101,
                    4'b0110: reg_write = 1'b1;
                    default: ;
                endcase
            end
            default: ;
        endcase
    end

    assign halted = (state == HALT);

endmodule


// ============================================================================
// MODULE: CPU (Datapath Top Level)
// ============================================================================
module cpu (
    input logic clk,
    input logic reset
);

    logic [7:0] registers [0:1];
    logic [7:0] PC;
    logic [7:0] IR;

    logic       halted;
    logic       ir_load;
    logic       pc_inc;
    logic       pc_branch;
    logic       pc_jump;
    logic       reg_write;
    logic       mem_write;
    logic       mem_sel;
    logic [1:0] alu_src;
    logic [1:0] alu_func;
    logic       latch_wb;
    logic       latch_is_mem;

    // ========================================================================
    // 1. Instruction decode
    // ========================================================================
    logic [3:0] opcode;
    logic       ds_idx;
    logic       s_idx;
    logic [7:0] imm_ext;
    logic [7:0] off_beq;
    logic [7:0] off_jmp;

    assign opcode  = IR[7:4];
    assign ds_idx  = IR[3];
    assign s_idx   = IR[2];

    assign imm_ext = {5'b00000, IR[2:0]};

    assign off_beq = {{4{IR[3]}}, IR[3:0]};
    assign off_jmp = {{4{IR[3]}}, IR[3:0]};

    // ========================================================================
    // 2. Memory
    // ========================================================================
    logic [7:0] reg_r1;
    logic [7:0] reg_r2;
    logic [7:0] mem_addr;
    logic [7:0] mem_data_out;

    assign mem_addr = mem_sel ? reg_r2 : PC;

    memory_module mem_inst (
        .clk      (clk),
        .addr     (mem_addr),
        .write_en (mem_write),
        .data_in  (reg_r1),
        .data_out (mem_data_out)
    );

    // ========================================================================
    // 3. Register file
    // ========================================================================
    assign reg_r1 = registers[ds_idx];
    assign reg_r2 = registers[s_idx];

    logic [7:0] wb_reg;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            registers[0] <= 8'h00;
            registers[1] <= 8'h00;
        end else if (reg_write) begin
            registers[ds_idx] <= wb_reg;
        end
    end

    // ========================================================================
    // 4. ALU + wb_reg latch
    // ========================================================================
    logic [7:0] alu_in_a;
    logic [7:0] alu_in_b;
    logic [7:0] alu_result;
    logic       alu_zero;

    assign alu_in_a = reg_r1;

    always_comb begin
        case (alu_src)
            2'b00:   alu_in_b = reg_r2;
            2'b01:   alu_in_b = mem_data_out;
            2'b10:   alu_in_b = imm_ext;
            default: alu_in_b = reg_r2;
        endcase
    end

    alu cpu_alu (
        .a      (alu_in_a),
        .b      (alu_in_b),
        .func   (alu_func),
        .result (alu_result),
        .zero   (alu_zero)
    );

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            wb_reg <= 8'h00;
        end else if (latch_wb) begin
            wb_reg <= latch_is_mem ? mem_data_out : alu_result;
        end
    end

    // ========================================================================
    // 5. Control unit
    // ========================================================================
    control_unit cu (
        .clk         (clk),
        .reset       (reset),
        .opcode      (opcode),
        .alu_zero    (alu_zero),
        .halted      (halted),
        .ir_load     (ir_load),
        .pc_inc      (pc_inc),
        .pc_branch   (pc_branch),
        .pc_jump     (pc_jump),
        .reg_write   (reg_write),
        .mem_write   (mem_write),
        .mem_sel     (mem_sel),
        .alu_src     (alu_src),
        .alu_func    (alu_func),
        .latch_wb    (latch_wb),
        .latch_is_mem(latch_is_mem)
    );

    // ========================================================================
    // 6. PC and IR
    // ========================================================================
    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            PC <= 8'h00;
            IR <= 8'h00;
        end else if (!halted) begin
            if (ir_load)
                IR <= mem_data_out;

            if (pc_inc)
                PC <= PC + 8'h01;
            else if (pc_branch)
                PC <= PC + off_beq;
            else if (pc_jump)
                PC <= PC + off_jmp;
        end
    end

endmodule