print("Enter values in the order: Principle, time, rate of interest !!! ")
pnr=[int(input()) for x in range(3)]
si=1
for i in pnr:
    si*=i
print("Simple Interest = ",si/100)