num=int(input("Enter array size: "))
print(f"Input {num} items : ")
lst=[int(input()) for x in range(num)]
rot=int(input('number of times to left rotate: '))
new=lst[rot:]+lst[:rot]
print(new)