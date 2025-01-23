def f(num):
    fib=[]
    for i in range (num):
        if i<=1:
            fib=fib+[i]
            print(fib[i])
        else:
           fib=fib+[fib[i-1]+fib[i-2]]
           print(fib[i], end=" ")

num=int(input("Enter no of terms:"))
print(f"Fibonacci upto {num} terms: ")
f(num)