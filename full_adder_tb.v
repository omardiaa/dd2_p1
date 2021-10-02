// file: full_adder_tb.v
`timescale 1ns/1ns


module full_adder_tb; 
reg  [5:0] a ;
reg  b ;
reg  cin ;
wire  sum;
wire  cout;



//Instantiation of Unit Under Test 
full_adder uut (
.a(a),
.b(b),
.cin(cin),
.sum(sum),
.cout(cout)); 
 
 
 initial begin 
//Inputs initialization 
a = 0; 
b = 0; 
cin = 0; 
//wait for the reset 
#100
end 
endmodule