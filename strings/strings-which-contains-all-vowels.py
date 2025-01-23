s=input("Enter a string: ")
vowels=['a','e','i','o','u']
count=0
absent=[]
for i in vowels:
    if i.upper() in s or i.lower()in s:
        count+=1
    else:
        absent+=[i]
if count!=5:
    print("Not Accepted")
    print("All vowels except '"+"','".join(absent)+"' are present")
else:
    print("Accepted \nAll vowels are present")