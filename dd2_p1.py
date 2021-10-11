import sys
import os
import hdlparse.verilog_parser as vlog

def parseInput():
    numberOfParameters = len(sys.argv)
    useRand = False
    clkpr= "5"
    rstpr= "50"
    terminatepr= "50"
    randomPeriod = "10"

    print(sys.argv)
    x=0
    for i in range(numberOfParameters):
        if(sys.argv[1]=="-rand"):
            useRand = True
            x=1
            randomPeriod = sys.argv[6]
        fileName = sys.argv[1+x]
        clkpr= sys.argv[2+x]
        rstpr= sys.argv[3+x]
        terminatepr= sys.argv[4+x]
        
    return {"fileName":fileName, "useRand": useRand, "clkpr":clkpr, "rstpr":rstpr,
    "terminatepr":terminatepr, "randomPeriod": randomPeriod}


def loadVLOGInputsAndOutputs(vlogObject):
    inputs=[]
    outputs=[]
    inouts=[]
    reg ="reg"
    none=" none" 
    for curPort in vlogObject.ports:
        if curPort.mode == "input":
            inputs.append({"name":curPort.name, "type":curPort.data_type})
        elif curPort.mode == "output":
            if (reg in curPort.data_type):
                curPort.data_type.replace('reg', '')
                outputs.append({"name":curPort.name, "type":curPort.data_type, "reg":reg})
            else:
                outputs.append({"name":curPort.name, "type":curPort.data_type, "reg":none})
        elif curPort.mode == "inout":
            inouts.append({"name":curPort.name, "type":curPort.data_type})
    return {"inputs":inputs,"outputs":outputs,"inouts":inouts}    


def write_tb(vlogObject, clkpr, rstpr, terminatepr, useRand, randomPeriod):
    x = loadVLOGInputsAndOutputs(vlogObject)
    clk = False 
    rst = False 
    rstname=""
    clkname=""
    print(x)
    with open(vlogObject.name + "_tb.v", 'w') as out:
        y = vlogObject.name + "_tb.v" 
        out.close()
        os.remove(y)

    with open(vlogObject.name + "_tb.v", 'w') as out:
        out.write("// file: " + vlogObject.name + "_tb.v" +  '\n' )
        out.write("`timescale 1ns/1ns" + '\n' + '\n' + '\n') 
        out.write("module " + vlogObject.name + "_tb; " + '\n') 
        for i in x['inputs']:
            out.write('reg ' + i['type'] + ' ' + i['name'] +  '_i ;' + '\n')
            if (((i['name'].lower()=="clk")|(i['name'].lower()=="clock"))):
                clk = True
                clkname=i['name'].lower()
            if (((i['name'].lower()=="rst")|(i['name'].lower()=="reset"))):
                rst = True
                rstname=i['name'].lower()
        for i in x['outputs']:
            if (i['reg']=="reg"):
                mm=i['type']
                mm=mm.replace('reg', '')
                out.write('wire' +mm+ ' ' + i['name'] +  '_o;' + '\n')
            else:
                out.write('wire' + i['type'] + ' ' + i['name'] +  '_o;' + '\n')               
        for i in x['inouts']:
            out.write('reg ' + i['type'] + ' ' + i['name'] +  '_io ;' + '\n')
            
        
        out.write("\n\nreg [31:0] counter;\ninitial begin \nforever#(1) counter = counter+1;\nend")

        if (clk): 
            out.write("\n\ninitial begin \n"+clkname+"_i =0; \nforever#("+ str(clkpr) +") "+clkname+"_i <= ~"+clkname+"_i ;\nend ")

        if (rst): 
            out.write("\n\ninitial begin \n"+rstname+"_i =0; \nforever#("+ str(rstpr) +") "+rstname+"_i <= ~"+rstname+"_i ;\nend ")


        out.write("\n" + "\n" + "\n" + "//Instantiation of Unit Under Test \n")
        out.write(vlogObject.name + " uut " + "("  + "\n") 
        
        for i in x['inputs']: 
            out.write("." + i['name'] + "(" + i['name'] + "_i)," + "\n")
        for i in x['outputs']: 
            out.write("." + i['name'] + "(" + i['name'] + "_o)," + "\n")  
        for i in x['inouts']: 
            out.write("." + i['name'] + "(" + i['name'] + "_io)," + "\n")  
        
    with open(y, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.close()

    with open(vlogObject.name + "_tb.v", 'a') as out:

        out.write("); \n \n \n ")
        out.write("initial begin\n$dumpfile(\""+vlogObject.name + "_tb"+".vcd\");\n$dumpvars;")
        out.write("\nend \n")

        out.write(" \n \n \n ")
        out.write("initial begin \n" + "//Inputs initialization \n") 
        out.write(" $monitor( \"") 
        for i in x['inputs']: 
            out.write(i['name']+"=%d,")
        for i in x['outputs']: 
            out.write(i['name']+"=%d,")

    with open(y, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.close()

    with open(vlogObject.name + "_tb.v", 'a') as out:
        out.write(" \", ")
        for i in x['inputs']: 
            out.write(i['name']+"_i,")
        for i in x['outputs']: 
            out.write(i['name']+"_o,") 

    with open(y, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.close()

    with open(vlogObject.name + "_tb.v", 'a') as out:
        out.write(" );\n")
        out.write("end\n\n\n")
        if useRand: 
            out.write("initial begin\n")
            for i in x['inputs']: 
                if((i['name'].lower()!="clk")&(i['name'].lower()!="clock")&(i['name'].lower()!="rst")&(i['name'].lower()!="reset")):
                    out.write(i['name'] + "_i = 0; \n")
            for i in x['inouts']: 
                out.write(i['name'] + "_o = 0; \n ") 

            out.write("forever#("+randomPeriod+")\n\nbegin\n")

            for i in x['inputs']: 
                if((i['name'].lower()!="clk")&(i['name'].lower()!="clock")&(i['name'].lower()!="rst")&(i['name'].lower()!="reset")):
                    out.write(i['name'] + "_i = $random; \n")
            for i in x['inouts']: 
                out.write(i['name'] + "_o = $random; \n ") 

            out.write("\nend\nend\n")

        else:
            out.write("initial begin\n")
            for i in x['inputs']: 
                if((i['name'].lower()!="clk")&(i['name'].lower()!="clock")):
                    out.write(i['name'] + "_i = 0; \n")
            for i in x['inouts']: 
                out.write(i['name'] + "_o = 0; \n ") 
            out.write("\nend\n\n")
        out.write("\n\n")
        out.write("initial begin\n")
        out.write("\nif(counter == "+terminatepr+")$finish;")
        
        out.write("\nend \nendmodule")

    with open(vlogObject.name + "_tb.v", 'r') as out:
        print(out.read())


def main():
    vlog_ex = vlog.VerilogExtractor()
    inputs = parseInput()
    vlogModules = vlog_ex.extract_objects(inputs["fileName"])
    
    for m in vlogModules:
        write_tb(m,inputs["clkpr"],inputs["rstpr"],inputs["terminatepr"], inputs["useRand"],inputs["randomPeriod"])
   




main()
