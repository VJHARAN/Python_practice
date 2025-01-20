#Find the contiguous subarray within a one-dimensional array of numbers which has the largest sum
import copy

def largest_sum(array,size,large):
    subarray=[]
    largest_subarray=[large]
    for i in range(size-1):                 #no of iterations
        for j in range(size-1-i):           #no of lists in each iteration
            for k in range(j,2+i+j):        #no of items in one list
                subarray=subarray+[array[k]]

            if sum(subarray)>large:
                large=sum(subarray)
                largest_subarray=[]
                largest_subarray=copy.copy(subarray)
            subarray=[]
    print("largest sum= ",large)
    # print("Largest contiguous subarray: ",largest_subarray)
    

#main
size=int(input("Input array size: "))
print(f"Enter a 1D array of {size} numbers separated by space:")
numbers=input().split()
numbers=[int(x) for x in numbers] 
count=0
large=0
for i in numbers: 
    if i <0:
        count+=1
if count==size: #if all items are negative values
    print("Invalid Input")
else: 
    print("1D array: ",numbers)
    for i in range(size):   #largest item in array
        if numbers[i]>large:
            large=numbers[i]
    largest_sum(numbers,size,large) #invoking the function
