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

def loadFile(fileName):
    with open(fileName) as f:
        lines = f.read()
    return lines


def main():
    inputs = parseInput()
    print(loadFile(inputs["fileName"]))

main()