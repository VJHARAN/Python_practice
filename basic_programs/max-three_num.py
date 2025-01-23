def large_three(*numbers):
    large=0
    for x in numbers:
        if x>large:
            large=x
    return large



a=int(input("Input First Num: "))
b=int(input("Second Num: "))
c=int(input("Third Num: "))
mx=large_three(a,b,c)
print(f"Largest of {a} {b} {c} is: {mx}")