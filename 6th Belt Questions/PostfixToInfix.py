# Practice

a = input().split()
stack = []

for i in a:
    if i in ['*', "+", '-', "/"]:
        op2 = stack.pop()
        op1 = stack.pop()
        b = "(" + op1 + " "+i+" "+op2+")"
        stack.append(b)

    else:
        stack.append(i)


print(stack.pop())