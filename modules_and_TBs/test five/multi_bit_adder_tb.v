// file: multi_bit_adder_tb.v
`timescale 1ns/1ns


module multi_bit_adder_tb; 
reg  [5:0] A_i ;
reg  [5:0] B_i ;
reg  cin_i ;
wire sum_o;
wire cout_o;


reg [31:0] counter;
initial begin 
forever#(1) counter = counter+1;
end


//Instantiation of Unit Under Test 
multi_bit_adder uut (
.A(A_i),
.B(B_i),
.cin(cin_i),
.sum(sum_o),
.cout(cout_o)); 
 
 
 initial begin
$dumpfile("multi_bit_adder_tb.vcd");
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
forever#(100)

begin
A_i = $random; 
B_i = $random; 
cin_i = $random; 

end
end


initial begin

if(counter == 800)$finish;
end 
endmodule