num=int(input("Enter array size: "))
print(f"Input {num} items : ")
lst=[int(input()) for x in range(num)]
sum=0
for i in lst:
    sum+=i
print("sum= ",sum)