num=int(input("Enter a list size: "))
lst=[int(input()) for x in range(num)]
print("Before: ",lst)
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print("After: ",lst)