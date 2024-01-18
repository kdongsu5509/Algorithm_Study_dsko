import sys

def order_push(stack, number):
    stack.append(int(number))
    return stack

def others(stack, order):
    if order[0] == "p":  # pop
        if len(stack) > 0:  # Check if the stack is not empty
            popped_value = stack.pop()
            sys.stdout.write(str(popped_value) + "\n")
        else:
            sys.stdout.write("-1\n")
    elif order[0] == "s":
        sys.stdout.write(str(len(stack)) + "\n")  # Exclude the initial -1 in the count
    elif order[0] == "t":
        if len(stack) > 0:  # Check if the stack is not empty
            sys.stdout.write(str(stack[-1]) + "\n")
        else:
            sys.stdout.write("-1\n")
    elif order[0] == "e":
        sys.stdout.write("0\n" if len(stack) > 0 else "1\n")

    return stack

stack = []

n = int(sys.stdin.readline().strip())
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack = order_push(stack, order[1])
    else:
        stack = others(stack, order[0])
