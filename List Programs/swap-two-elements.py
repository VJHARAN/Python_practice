num=int(input("Enter a list size: "))
lst=[int(input()) for x in range(num)]
pos=[int(input(f"Enter position {x+1}: ")) for x in range(2)]
print("Before: ",lst)
lst[pos[0]-1],lst[pos[1]-1]=lst[pos[1]-1],lst[pos[0]-1]
print("After: ",lst)