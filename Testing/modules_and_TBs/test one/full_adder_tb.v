// file: full_adder_tb.v
`timescale 1ns/1ns


module full_adder_tb; 
reg  A_i ;
reg  B_i ;
reg  cin_i ;
wire sum_o;
wire cout_o;


reg [31:0] counter;
initial begin 
forever#(1) counter = counter+1;
end


//Instantiation of Unit Under Test 
full_adder uut (
.A(A_i),
.B(B_i),
.cin(cin_i),
.sum(sum_o),
.cout(cout_o)); 
 
 
 initial begin
$dumpfile("full_adder_tb.vcd");
$dumpvars;
end 
 
 
 
 initial begin 
//Inputs initialization 
 $monitor( "A=%d,B=%d,cin=%d,sum=%d,cout=%d ", A_i,B_i,cin_i,sum_o,cout_o );
end


initial begin
A_i = 0; 
B_i = 0; 
cin_i = 0; 

end



initial begin

if(counter == 800)$finish;
end 
endmodule