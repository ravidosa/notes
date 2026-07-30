module vending_machine (
    input  logic clk,
    input  logic rst_n,    // Active low reset
    input  logic nickel,   // 5 cents
    input  logic dime,     // 10 cents
    output logic dispense, // Merchandise out
    output logic change    // 5 cent nickel change
);
    reg [5:0] curr;
    reg [5:0] next;

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            curr <= 0;
        end
        else begin
            curr <= next;
        end
    end

    always @(*) begin
        if (nickel) begin
            next = curr + 5;
        end
        else if (dime) begin
            next = curr + 10;
        end
        else begin
            next = curr;
        end
        if (next >= 30) begin
            dispense = 1;
            change = (next == 35) ? 1'b1 : 1'b0;
            next = 1'b0;
        end
        else begin
            dispense = 1'b0;
            change = 1'b0;
        end
    end

endmodule