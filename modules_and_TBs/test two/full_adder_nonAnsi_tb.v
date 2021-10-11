// file: full_adder_nonAnsi_tb.v
`timescale 1ns/1ns


module full_adder_nonAnsi_tb; 
reg  a_i ;
reg  b_i ;
reg  cin_i ;
wire sum_o;
wire cout_o;


reg [31:0] counter;
initial begin 
forever#(1) counter = counter+1;
end


//Instantiation of Unit Under Test 
full_adder_nonAnsi uut (
.a(a_i),
.b(b_i),
.cin(cin_i),
.sum(sum_o),
.cout(cout_o)); 
 
 
 initial begin
$dumpfile("full_adder_nonAnsi_tb.vcd");
$dumpvars;
end 
 
 
 
 initial begin 
//Inputs initialization 
 $monitor( "a=%d,b=%d,cin=%d,sum=%d,cout=%d ", a_i,b_i,cin_i,sum_o,cout_o );
end


initial begin
a_i = 0; 
b_i = 0; 
cin_i = 0; 

end



initial begin

if(counter == 800)$finish;
end 
endmodule