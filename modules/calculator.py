import adder as a
import subtractor as s
import product as p
import divider as d

print(5*" "+"Calculator")
print(20*"=")
domore='y'
while domore!='n':
    choice=int(input("\n\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter your choice:- "))
    if choice in [1,2,3,4]:
        num1=int(input("Enter numbers: "))
        num2=int(input())
        if choice==1:
            result=a.add(num1,num2)
            print("Sum = ",result)
        elif choice==2:
            result=s.subtract(num1,num2)
            print("Difference = ",result)
        elif choice==3:
            result=p.multiply(num1,num2)
            print("Product = ",result)
        elif choice==4:
            result=d.divide(num1,num2)
            print("Quotient = ",result)
        else:
            pass
    else:
        print("Wrong choice!")
    domore=input("Do you wish to continue ? (y/n)")