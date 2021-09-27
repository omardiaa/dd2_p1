`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
//For testing 
//////////////////////////////////////////////////////////////////////////////////

module full_adder (
   a,
   b,
   cin,
   sum,
   cout
);
   input  a;
   input  b;
   input  cin;
   output sum;
   output cout;
   
   assign {cout,sum} = a+b+cin;
  
endmodule

