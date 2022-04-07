import sys

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Error: Please provide the target .rsl filepath as an argument.")
        sys.exit()
    if len(sys.argv) > 2:
        print("Error: Too many arguements. Expected 1, the .rsl filepath, Received: " + len(sys.argv))
        sys.exit()
    
    if not isinstance(sys.argv[0], str):
        print("Error: Expected command line argument to be a string")
        sys.exit()
        

    path = sys.argv[1]
    try:
        with open(path) as f:
            print("File open")
            lines = f.readlines()
            tokens = tokenize(lines)


    except:
        print("Error: Failed to read file")

def tokenize(lines):
    inStates = False
    inValues = False
    inTransitions = False

    states = []
    valueNames = []
    valueInit = []
    transitions= []

    for line in lines:
        print(line)
        tokens = line.split()
        print(tokens)
        length = len(tokens)
        #Check if empty line
        if length == 0:
            continue

        #Check for start of state
        if length == 1 and tokens[0] == "STATES":     
            inStates = True
            continue
        
        #Check for start of values
        if length == 1 and tokens[0] == "VALUES":       
            inValues = True
            inStates = False
            continue

        #Check for start of transitions
        if length == 1 and tokens[0] == "TRANSITIONS":
            inTransitions = True
            inValues = False
            continue

        #Add states
        if inStates == True:
            states.append(tokens[0])
            continue

        #Add values
        if inValues == True:
            valueNames.append(tokens[0])
            valueInit.append(tokens[1])
            continue

        #Add transitions
        if inTransitions == True:
            if length == 3 and tokens[1] == "->":
                transitions.append('if LAST_STATE == "' + tokens[0] + '":' )
                transitions.append('    ' + tokens[2] + '.main()')
                transitions.append('    LAST_STATE = "' + tokens[2] + '"')
                transitions.append('    continue')
                transitions.append('    ')
    
    parse(states, valueNames, valueInit, transitions)
        
def parse(states, valueNames, valueInit, transitions):
    print(valueNames)
    print(valueInit)
    f = open("Robot.py", "w")
    for state in states:
        f.write('import ' + state + '\n')
    


    f.write("\n")
    f.write('LAST_STATE = "START"\n')

    for i in range(0, len(valueNames)):
        f.write(valueNames[i] + ' = ' + valueInit[i] + '\n')
    
    f.write("\n")
    f.write("while True:\n")
    for transition in transitions:
        f.write('    ' + transition + '\n')
    
    f.write('    break')



if __name__ == "__main__":
    main()