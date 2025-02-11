#  Print All Odd Numbers in a Range

limit=list(map(int,input("Enter a range: ").strip().split()))
print(f"odd numbers in {limit} are : ",end=" ")
for i in range(limit[0],limit[1]):
    if i%2!=0:
        print(i,end="  ")
