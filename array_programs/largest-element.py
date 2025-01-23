num=int(input("Enter array size: "))
print(f"Input {num} items : ")
lst=[int(input()) for x in range(num)]
for i in range(num):
    for j in range(i+1,num):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("Largest item= ",lst[-1])