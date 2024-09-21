# Error 


infix = input().strip() 

infix = infix[::-1] 
infix = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in infix])
stack = []
prefix = []

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

for i in infix:
    if i.isdigit():
        prefix.append(i)
    elif i == ')':
        stack.append(i)
    elif i == '(':
        while stack and stack[-1] != ')':
            prefix.append(stack.pop())
        stack.pop() 
    else:
        while (stack and stack[-1] != ')' and precedence.get(stack[-1], 0) >= precedence[i]):
            prefix.append(stack.pop())
        stack.append(i)
while stack:
    prefix.append(stack.pop())

prefix = ''.join(prefix[::-1])
print(prefix)
