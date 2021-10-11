// file: DFlipFlop_tb.v
`timescale 1ns/1ns


module DFlipFlop_tb; 
reg  clk_i ;
reg  rst_i ;
reg  D_i ;
wire Q_o;


reg [31:0] counter;
initial begin 
forever#(1) counter = counter+1;
end

initial begin 
clk_i =0; 
forever#(10) clk_i <= ~clk_i ;
end 

initial begin 
rst_i =0; 
forever#(100) rst_i <= ~rst_i ;
end 


//Instantiation of Unit Under Test 
DFlipFlop uut (
.clk(clk_i),
.rst(rst_i),
.D(D_i),
.Q(Q_o)); 
 
 
 initial begin
$dumpfile("DFlipFlop_tb.vcd");
$dumpvars;
end 
 
 
 
 initial begin 
//Inputs initialization 
 $monitor( "clk=%d,rst=%d,D=%d,Q=%d ", clk_i,rst_i,D_i,Q_o );
end


initial begin
D_i = 0; 
forever#(100)

begin
D_i = $random; 

end
end


initial begin

if(counter == 800)$finish;
end 
endmodule