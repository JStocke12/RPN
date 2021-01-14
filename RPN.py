print("Enter an input to be evaluated in Reverse Polish Notation:")

RPNInput = []

RPNOutput = []

OpList = {'+':lambda x, y: y + x,'-':lambda x, y: y - x,'*':lambda x, y: y * x,'/':lambda x, y: y / x,'^':lambda x, y: y ** x}

SubList = {"clear":"0 * +", "negate":"-1 *", "invert":"-1 ^"}
CharSubList = {key[0]:value for (key,value) in SubList.items()}

while True:
    if RPNInput == []:
        if RPNOutput != []:
            print(RPNOutput[-1])
        [RPNInput.append(j) for j in input("> ").split()]
    else:
        i = RPNInput.pop(0).lower()
        try:
            RPNOutput.append(float(i))
        except:
            if i == "print" or i == "p":
                print(RPNOutput)
            elif i == "exit" or i == "x":
                break
            elif i == "sqrt":
                approx = 1
                val = RPNOutput.pop()
                while abs(approx**2 - val) > 10**-15:
                    approx = (approx + val/approx)/2
                RPNOutput.append(approx)
            elif i in OpList:
                RPNOutput.append(OpList[i](RPNOutput.pop(),RPNOutput.pop()))
            elif i in SubList:
                [RPNInput.insert(0, j) for j in SubList[i].split()[::-1]]
            elif i in CharSubList:
                [RPNInput.insert(0, j) for j in CharSubList[i].split()[::-1]]
