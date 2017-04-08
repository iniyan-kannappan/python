ClassMarks=['Math','Writing','History','Science']
BillMarks=[86,80,78,94]
TomMarks=[65,78,79,87]
MikeMarks=[89,76,87,75]
Total=[ClassMarks,BillMarks,TomMarks,MikeMarks]
print(Total)
print('TomMarks for History:',Total[2][2])
sum=0
count=0
print('Enter a subject:')
##print(Total[0][0])
##print(Total[1][0])
##print(Total[2][0])
##print(Total[3][0])
subject=input()
if subject=='Math' or subject=='math':
   sum=0
   count=0
   for r in range(1,4,1):
        sum=sum+Total[r][0]
        count=count+1
   print('Sum ',sum,'Count ',count)
   print('Average',sum/count)
elif subject=='Writing' or subject=='writing':
    sum=0
    count=0
    for r in range(1,4,1):
        sum=sum+Total[r][1]
        count=count+1
    print('Sum ',sum,'Count ',count)
    print('Average',sum/count)
elif subject=='History' or subject=='history':
    sum=0
    count=0
    for r in range(1,4,1):
        sum=sum+Total[r][2]    
        count=count+1
    print('Sum ',sum,'Count ',count)
    print('Average',sum/count)
elif subject=='Science' or subject=='science':
    sum=0
    count=0
    for r in range(1,4,1):
        sum=sum+Total[r][3]    
        count=count+1
    print('Sum ',sum,'Count ',count)
    print('Average',sum/count)



