import time
print('How many seconds?')
seconds=int(input())
for loop in range(seconds,0,-1):
    print(loop)
    time.sleep(1)
print('Blast Off!')
