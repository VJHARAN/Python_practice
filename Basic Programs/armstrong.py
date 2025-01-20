num=input("Enter a number: ")
dig=[int(x) for x in num]
l=len(dig)
tot=0

for i in range(l):
    tot=tot+int(dig[i])**l

res=print(f"{num} IS an Armstrong number!") if tot==int(num) else print(f"{num} is NOT an Armstrong number !") 
