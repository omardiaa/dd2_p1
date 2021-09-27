import sys
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
    for curObject in vlogObject:
        for curPort in curObject.ports:
            if curPort.mode == "input":
                inputs.append({"name":curPort.name, "type":curPort.data_type})
            elif curPort.mode == "output":
                outputs.append({"name":curPort.name, "type":curPort.data_type})
            elif curPort.mode == "inout":
                inouts.append({"name":curPort.name, "type":curPort.data_type})
    return {"inputs":inputs,"outputs":outputs,"inouts":inouts}    


def main():
    vlog_ex = vlog.VerilogExtractor()
    inputs = parseInput()
    vlogObject = vlog_ex.extract_objects(inputs["fileName"])
    print(loadVLOGInputsAndOutputs(vlogObject))

main()