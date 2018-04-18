stack = list()
top = 0

stack.append(4)
top += 1

stack.append(9)
top += 1

print(stack)
print(top)


del stack[top - 1]
print(stack)
