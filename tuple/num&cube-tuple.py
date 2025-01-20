print("Input a list of 6 numbers")
lst1=[int(input()) for x in range(6)]
lst2=[(x,x**3) for x in lst1]
print(lst2)
tup=(9,8)
lst1=lst1+list(tup)
print(lst1)