// file: full_adder_tb.v
`timescale 1ns/1ns


module full_adder_tb; 
reg  [5:0] a_i ;
reg  b_i ;
reg  cin_i ;
reg  clk_i ;
reg  rst_i ;
wire  sum_o;
wire  cout_o;


initial begin 
clk_i =0; 
forever#(10) clk_i <= ~clk_i ;
end 

initial begin 
rst_i =0; 
forever#(100) rst_i <= ~rst_i ;
end 


//Instantiation of Unit Under Test 
full_adder uut (
.a(a_i),
.b(b_i),
.cin(cin_i),
.clk(clk_i),
.rst(rst_i),
.sum(sum_o),
.cout(cout_o)); 
 
 
 initial begin
$dumpfile("full_adder_tb.vcd");
$dumpvars;
end 
 
 
 
 initial begin 
//Inputs initialization 
 $monitor( "a=%d,b=%d,cin=%d,clk=%d,rst=%d,sum=%d,cout=%d ", a_i,b_i,cin_i,clk_i,rst_i,sum_o,cout_o );

a_i = 0; 
b_i = 0; 
cin_i = 0; 
rst_i = 0; 
//wait for the reset 
#100
#800
$finish
end 
endmodule