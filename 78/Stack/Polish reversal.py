def evalRPN(tokens):
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)   # truncates toward zero
    }

    for t in tokens:
        if t not in ops:# by defualt, the key of the dictioanry is checked
            stack.append(int(t))
        else:
            b=stack.pop()
            a=stack.pop()
            stack.append(ops[t](a, b))#Call that function with arguments a and b.
    return stack[-1]                           
                    
      



print(evalRPN(["1","2","+","3","*","4","-"]))

#b = stack.pop()
#a = stack.pop()
'''these basically mean remove the two number before and save them at the same time'''

#else: stack.append(int(t))
'''If the token isn’t an operator, it’s a number — turn it into an integer and put it on the stack.'''

#stack.append(ops[t](a, b))
'''“Find the math operation for t, run it on a and b, then put the result back on the stack.”'''
