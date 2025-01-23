import adder as a



print(5*" "+"Calculator")
print(20*"=")
domore='y'
while domore!='n':
    choice=int(input("\n\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter your choice:- "))
    num1=int(input("Enter numbers: "))
    num2=int(input())
    if choice==1:
        result=a.add(num1,num2)
        print("Sum = ",result)
    domore=input("Do you wish to continue ? (y/n)")