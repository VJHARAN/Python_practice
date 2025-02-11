#Check Whether a Given Number is Even or Odd using Recursion
def even_or_odd(x):
    if x<2:
        return "Even" if x%2==0 else "Odd"
    else:
        return even_or_odd(x-2)




n=int(input("Enter a number: "))
print(f"{n} is {even_or_odd(n)} !")