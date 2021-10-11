To run the program, enter the following command on the terminal in the target directory:

python3 dd2_p1.py %target_module.v% clkperiod rstperiod termination randperiod
for example:
dd2_p1.py full_adder.v 10 100 800 100

to run using randomization:

python3 dd2_p1.py -rand  %target_module.v% clkperiod rstperiod termination randperiod
for example:
python3 dd2_p1.py -rand DFlipFlop.v 10 100 800 100


Test cases:

Case one: covering normal testbench creation of a normal combinational module
Run dd2_p1.py full_adder.v 10 100 800 100

Case two: covering normal testbench creation of a normal combinational module, using a non-Ansi type module
Run python3 dd2_p1.py full_adder_nonAnsi.v 10 100 800 100


Case three: covering a sequential testbench of a flipflop module
Run python3 dd2_p1.py DFlipFlop.v 10 100 800 100

Case four: covering a sequential testbench of a flipflop module, with randomization of inputs, with output reg type enabled
Run python3 dd2_p1.py -rand DFlipFlop.v 10 100 800 100


Case five: covering multi-bit ports, with randomization enabled
Run python3 dd2_p1.py -rand multibit.v 10 100 800 100
