`timescale 1us/1us

module fake_crypto (
  input logic clk,
  input logic [7:0] input_,
  output logic [7:0] output_
);

always @(posedge clk) begin
  output_ <= ~input_;
end

// Dump waves
initial begin
  $dumpfile("dump.vcd");
  $dumpvars(1, fake_crypto);
end

endmodule
