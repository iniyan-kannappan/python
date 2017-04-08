lis=[]
for loop in range(1,1000,1):
    n=(input())
    w=n.split(" ")
    if w[0]=='insert':
        lis.insert(int(w[1]),int(w[2]))
    elif w[0]=='sort':
        lis.sort()
    elif w[0]=='reverse':
        lis.reverse()
    elif w[0]=='print':
        print(lis)
    elif w[0]=='remove':
        lis.remove(int(w[1]))
    elif w[0]=='append':
         lis.append(int(w[1]))
    elif w[0]=='pop':
         lis.pop(int(w[1]))
