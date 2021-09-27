# dd2_p1

#### How to run?
 - tbgen -rand input_verilog_file_name

#### Inputs:
 
 - Given a Sequential Module:
    - tbgen -rand input_verilog_file_name
 - Given a Combination Module:
    - tbgen -rand rstAssertionDuration input_verilog_file_name
### Outputs:
 
- A printed Test Bench Program on the terminal following the following guide
    - The test bench name is the same module name + _tb
    - Timescale is defined to be: 1ns/1ps
    - Wires and variables of type reg are created to be mapped to the module's inputs. Registers have the same name as the input ports prefixed with _i and wires have the same name as the output ports prefixed with _o. Registers are initialized to zero.
    - If the input contains the words (rst or reset and clk or clock), the code creates the corresponding clock in the test bench. The reset assertion duration is parameter to the testbench.
    - The test bench instantiates the Module and pass the appropriate parameters.
    - The testbench dumbs the changes in all signals for all hierarchy levels into a file named after the testbench name (.vcd extension)
    - If rand parameter is passed to the terminal, random test benches will be generated.
    - 
