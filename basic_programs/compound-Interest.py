print("Enter values in the order: Principle, time, rate of interest !!! ")
pnr=[int(input()) for x in range(3)]
ci=1   
x=pnr[0]
ci=pnr[0]*1*pnr[2]/100  
pnr[0]=ci+pnr[0]                   
for i in range(pnr[1]-1):
    p=pnr[0]*pnr[2]/100
    pnr[0]=pnr[0]+p
ci=pnr[0]-x
print("Compound Interest = ",ci,"\nTotal amount= ",pnr[0])
