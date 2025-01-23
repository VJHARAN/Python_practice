def fib(x):
    if x<=1:
        return x
    else:
        return fib(x-1)+fib(x-2)

num=int(input("Enter no of terms:"))
if num<=0:
    print("Positive integer expected!")
else:
    for i in range(num):
        print(fib(i), end=" ")