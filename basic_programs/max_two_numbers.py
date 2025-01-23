numbers=[int(input(f"Enter number{x}: ")) for x in range(1,3)]
large= numbers[0] if numbers[0]>numbers[1] else numbers[1]
print(f"Maximum of {numbers[0]} & {numbers[1]} is:",large)