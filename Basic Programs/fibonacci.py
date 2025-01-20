num=int(input("Enter the number: "))
lst=[]
if num<3:
    if num==1:
        lst+=[0]
    elif num==2:
        lst+=[0,1]
    print(f"{num}th fibonacci number= ",lst[-1])
else:
    lst+=[0,1]
    for i in range(2,num+1):
        lst=lst+[lst[i-1]+lst[i-2]]
print(lst)
print(f"{num}th fibonacci number= ",lst[-1])