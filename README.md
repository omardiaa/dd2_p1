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


#### Problems:
- The program does not support error checking on the target module; thus make sure you have a well structured target module before running the testbench creator.
- if provided "input wire" instead of input, the resulting testbench would have a problem in declairing the port, thus make sure to have inputs as "input" not "input wire", which is technically the same.

#### Contributors:
- Youssef Ashraf Kandil
- Mohamed Aly Ellethy
- Omar Diaa El-Dessouky