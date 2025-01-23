num=int(input("Enter a limit: "))
sum=0
for i in range(1,num+1):
    sum+=i**3
print(f"sum of cubes of 1st {num} natural numbers= ",sum)