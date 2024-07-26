`timescale 1ns / 1ps

module half_adder (
    input  logic a_i,
    input  logic b_i,
    output logic sum_o,
    output logic carry_o
);

always_comb begin
    sum_o = a_i & b_i;
    carry_o = a_i & b_i;
end
    
endmodule

//asds
