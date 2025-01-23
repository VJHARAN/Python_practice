def fact(f):
    return 1 if f<=1 else f*fact(f-1)



num=int(input("Enter a number:"))
print(f"Factorial of {num} is",fact(num))