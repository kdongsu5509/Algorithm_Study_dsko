# 묻따 등차수열

x = int(input())

def find_step(x):
    total = 0
    for a in range(1, x+1):
        total += a
        if total >= x:
            return a, total - a
        
step, key = find_step(x)

body = str(x - key)
head = str((step + 1) - int(body))

if(step % 2 == 1):
    print(head + '/' + body)
else:
    print(body+'/'+head)
# print(head,'/', body)s
        

