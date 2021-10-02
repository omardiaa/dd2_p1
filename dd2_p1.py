import sys
import os
import hdlparse.verilog_parser as vlog

def parseInput():
    numberOfParameters = len(sys.argv)
    useRand = False

    for i in range(numberOfParameters):
        if(sys.argv[i]=="-rand"):
            useRand = True
        else:
            fileName = sys.argv[i]
    return {"fileName":fileName, "useRand": useRand}


def loadVLOGInputsAndOutputs(vlogObject):
    inputs=[]
    outputs=[]
    inouts=[]
    
    for curPort in vlogObject.ports:
        if curPort.mode == "input":
            inputs.append({"name":curPort.name, "type":curPort.data_type})
        elif curPort.mode == "output":
            outputs.append({"name":curPort.name, "type":curPort.data_type})
        elif curPort.mode == "inout":
            inouts.append({"name":curPort.name, "type":curPort.data_type})
    return {"inputs":inputs,"outputs":outputs,"inouts":inouts}    


def write_tb(vlogObject):
    
    x = loadVLOGInputsAndOutputs(vlogObject)
    z = False 
    with open(vlogObject.name + "_tb.v", 'w') as out:
        y = vlogObject.name + "_tb.v" 
        os.remove(y) 
    print (x) 
    with open(vlogObject.name + "_tb.v", 'w') as out:
        out.write("// file: " + vlogObject.name + "_tb.v" +  '\n' )
        out.write("`timescale 1ns/1ns" + '\n' + '\n' + '\n') 
        out.write("module " + vlogObject.name + "_tb; " + '\n') 
        for i in x['inputs']:
            out.write('reg ' + i['type'] + ' ' + i['name'] +  ' ;' + '\n')
            if (i['name']=="clk"):
                z = True
        for i in x['outputs']:
            out.write('wire ' + i['type'] + ' ' + i['name'] +  ';' + '\n')
        for i in x['inouts']:
            out.write('reg ' + i['type'] + ' ' + i['name'] +  ' ;' + '\n')
       
       
        if (z): 
            out.write("\n\ninitial begin \nclk =0; \nforever#(5) clk<=~clk;\nend ")
         



        out.write("\n" + "\n" + "\n" + "//Instantiation of Unit Under Test \n")
        out.write(vlogObject.name + " uut " + "("  + "\n") 
        
        for i in x['inputs']: 
            out.write("." + i['name'] + "(" + i['name'] + ")," + "\n")
        for i in x['outputs']: 
            out.write("." + i['name'] + "(" + i['name'] + ")," + "\n")  
        for i in x['inouts']: 
            out.write("." + i['name'] + "(" + i['name'] + ")," + "\n")  
        
    with open(y, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
        filehandle.close()

    with open(vlogObject.name + "_tb.v", 'a') as out:
        out.write("); \n \n \n ")
        out.write("initial begin \n" + "//Inputs initialization \n") 

        for i in x['inputs']: 
            if(i['name']!="clk"):
                out.write(i['name'] + " = 0; \n")
        for i in x['inouts']: 
            out.write(i['name'] + " = 0; \n ") 
        out.write("//wait for the reset \n#100")
        out.write("\nend \nendmodule")


def main():
    vlog_ex = vlog.VerilogExtractor()
    inputs = parseInput()
    vlogModules = vlog_ex.extract_objects(inputs["fileName"])
    

    for m in vlogModules:
        write_tb(m)
   




main()
