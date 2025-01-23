num=int(input("Enter array size: "))
print(f"Input {num} items : ")
lst=[int(input()) for x in range(num)]
flag=True
for i in range(num):
    if i+2<num:
        if lst[i+1]!=(lst[i]+lst[i+2])/2:
            flag=False
            break
x=print("monotonous") if flag==True else print("Not monotonous")