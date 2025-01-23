string=input("Enter a string: ")
print("Palindrome") if string==string[::-1] else print("Not Palindrome")
l=len(string)
if l%2==0:
    l=int(l/2)
    if string[:l]==string[l:]:
        print("Symmetrical")
else:
    print("Not Symmetrical")