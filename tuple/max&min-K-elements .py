print("Input a tuple of numbers: ")

lst=[int(input()) for x in range(6)]
k=int(input("input K"))
tup=tuple(lst)
lst=list(sorted(tup))
lst=tuple(lst)
res=[]
for i in range(k):
    res.append(lst[i])
for i in range(5,3,-1):
    res.append(lst[i])
res.sort()
res=tuple(res)
print(res)
