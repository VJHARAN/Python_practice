str1=input("Enter the 1st string: ")
str2=input("Enter the 2nd string: ")
str1=list(str1)
str2=list(str2)
res=[x for x in str1 if x in str2]
print("No.of matching characters = ",len(res))