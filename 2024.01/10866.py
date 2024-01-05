import sys
from queue import deque

def order_push(Deque, order, number):
    if order == "push_front":
        Deque.appendleft(number)
    else:
        Deque.append(number)

def order_another(Deque, order):
    if order[0] == "b": #back 명령
        if len(Deque) < 1:
            sys.stdout.write("-1\n")
        else:
            # print(Deque[-1])
            sys.stdout.write((str(Deque[-1])) + "\n")
    elif order[0] == "f": #front 명령
        if len(Deque) < 1:
            sys.stdout.write("-1\n")
        else:
            # print(Deque[0])
            sys.stdout.write((str(Deque[0])) + "\n")
            
    elif order[0] == "e": #empty 명령
        if len(Deque) < 1:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif order[0] == "s": #size 명령
        sys.stdout.write(str(len(Deque)) + "\n")
    else:
        if order == "pop_back" and len(Deque) > 0:
            popped_value = Deque.pop()
            # print(pop_number)
            sys.stdout.write(str(popped_value) + "\n")
        elif order == "pop_front" and len(Deque) > 0:
            popped_value = Deque.popleft()
            # print(pop_number)
            sys.stdout.write(str(popped_value) + "\n")
        else:
            sys.stdout.write("-1\n")
            




n = int(input())

DEQUE = deque()

last_print = []

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == "push_back" or order[0] == "push_front":
        order_push(DEQUE, order[0], order[1])
    else:
        order_another(DEQUE, order[0])

