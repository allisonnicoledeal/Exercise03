
import arithmetic

done = False

while not done:
    print "Enter arguments"
    argument = raw_input()
    tokens = argument.split(" ")


    if tokens[0] == "+":
        print arithmetic.add(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "-":
        print arithmetic.subtract(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "*":
        print arithmetic.multiply(int(tokens[1]),int(tokens[2]))    
    elif tokens[0] == "/":
        print arithmetic.divide(int(tokens[1]),int(tokens[2]))    
    elif tokens[0] == "^2":
        print arithmetic.square(int(tokens[1]))  
    elif tokens[0] == "^3":
        print arithmetic.cube(int(tokens[1]))
    elif tokens[0] == "pow":
        print arithmetic.power(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "%":
        print arithmetic.mod(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "q":
        done = True
    else:
        print "Not a valid argument"              