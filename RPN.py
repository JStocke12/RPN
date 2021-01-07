print("Enter an input to be evaluated in Reverse Polish Notation:")

RPNInput = []

RPNOutput = []

OpList = {'+':lambda x, y: y + x,'-':lambda x, y: y - x,'*':lambda x, y: y * x,'/':lambda x, y: y / x,'^':lambda x, y: y ** x}

SubList = {"clear":"0 * +"}

while True:
    if RPNInput == []:
        [RPNInput.append(j) for j in input("> ").split()]
    else:
        i = RPNInput.pop(0).lower()
        try:
            RPNOutput.append(float(i))
        except:
            if i == "print":
                print (val := RPNOutput.pop())
                RPNOutput.append(val)
            elif i == "exit":
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
                [RPNInput.append(j) for j in SubList[i].split()]
