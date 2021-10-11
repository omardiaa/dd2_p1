# dd2_p1

#### How to run?
 - To run the program, enter the following command on the terminal in the target directory:

    - python3 dd2_p1.py %target_module.v% clkperiod rstperiod termination randperiod
      - for example:
      - dd2_p1.py full_adder.v 10 100 800 100

- To run using randomization:

   - python3 dd2_p1.py -rand  %target_module.v% clkperiod rstperiod termination randperiod
      - for example:
      - python3 dd2_p1.py -rand DFlipFlop.v 10 100 800 100

#### Outputs:
 
- A test bench file and a printed Test Bench Program on the terminal following the following guide
    - The test bench name is the same module name + _tb
    - Timescale is defined to be: 1ns/1ps
    - Wires and variables of type reg are created to be mapped to the module's inputs. Registers have the same name as the input ports prefixed with _i and wires have the same name as the output ports prefixed with _o. Registers are initialized to zero.
    - If the input contains the words (rst or reset and clk or clock (case insensitive)), the code creates the corresponding clock in the test bench. The reset assertion duration is parameter to the testbench.
    - The test bench instantiates the Module and pass the appropriate parameters.
    - The testbench dumbs the changes in all signals for all hierarchy levels into a file named after the testbench name (.vcd extension)
    - If rand parameter is passed to the terminal, random test benches will be generated.

#### Dependencies:
- To run the program, you need to have the following library installed on your device and running.
    - import hdlparse.verilog_parser as vlog.
    - you can find the library installation and documentation in the following link:
        + Hdlparse: https://kevinpt.github.io/hdlparse/ .
    - this library is responsible for parsing the file containing the target module, providing an array of module   objects holding the ports, parameters, and module name.


#### How the code works? 

- vlog_ex = vlog.VerilogExtractor()
+ VerilogExtractor is an extractor class and is the main mechanism of the Hdlparse library. After creating this mechanism, we go and take the terminal inputs being the file name of the Verilog module we want to operate the test bench on, the termination time, the clock period, the optional -rand for generating alternating random values for the regs along with a period at which these random variables are generated and we parse the input in the variable “inputs” by taking the return value of the function parseInput(), which has the aforementioned functionality. We then call the built in library function .extract_objects() that we pass to the file name parsed from the previous function so that it could automate the generation of its testbench. 

+ Afterwards, we then iterate on the variable vlogModules that takes the return value of the function .extract_objects(), as a file could contain more than one module that will be parsed in different objects. We pass this object to the function write_tb(), along with the terminal arguments that will be used for clk generation in case the we have a clock, reset generation in case we have reset, random generation in case we have -rand and the randomPeriod. In this function we start by printing out the module name, which is the same as the file name concatenated with _tb.v and then we iterate on the inputs, turn them into regs, outputs into wires. Upon the flags/arguments passed by from the terminal, a decision is taken to implement the aforementioned functionalities. We also make sure to monitor all ports using $monitor and dumb the changes in all signals into a .vcd file.//


#### Problems:
- The program does not support error checking on the target module; thus make sure you have a well structured target module before running the testbench creator.
- if provided "input wire" instead of input, the resulting testbench would have a problem in declairing the port, thus make sure to have inputs as "input" not "input wire", which is technically the same.

#### Test cases:
- Case one: covering normal testbench creation of a normal combinational module
    + Run dd2_p1.py full_adder.v 10 100 800 100

- Case two: covering normal testbench creation of a normal combinational module, using a non-Ansi type module
    + Run python3 dd2_p1.py full_adder_nonAnsi.v 10 100 800 100

- Case three: covering a sequential testbench of a flipflop module
    + Run python3 dd2_p1.py DFlipFlop.v 10 100 800 100

- Case four: covering a sequential testbench of a flipflop module, with randomization of inputs, with output reg type enabled
    + Run python3 dd2_p1.py -rand DFlipFlop.v 10 100 800 100

- Case five: covering multi-bit ports, with randomization enabled
    + Run python3 dd2_p1.py -rand multibit.v 10 100 800 100

#### Contributors:
- Youssef Ashraf Kandil
- Mohamed Aly Ellethy
- Omar Diaa El-Dessouky