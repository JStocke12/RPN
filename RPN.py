print("Enter an input to be evaluated in Reverse Polish Notation:")

RPNInput = []

RPNOutput = []

OpList = {'+':lambda x, y: y + x,'-':lambda x, y: y - x,'*':lambda x, y: y * x,'/':lambda x, y: y / x,'^':lambda x, y: y ** x}

SubList = {'c':"0 * +"}

while True:
    if RPNInput == []:
        [RPNInput.append(j) for j in input("> ").split()]
    else:
        i = RPNInput.pop(0)
        try:
            RPNOutput.append(float(i))
        except:
            if i == 'p':
                print (val := RPNOutput.pop())
                RPNOutput.append(val)
            elif i == 'x':
                break
            elif i in OpList:
                RPNOutput.append(OpList[i](RPNOutput.pop(),RPNOutput.pop()))
            elif i in SubList:
                [RPNInput.append(j) for j in SubList[i].split()]
