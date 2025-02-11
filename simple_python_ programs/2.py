# Check Whether a Number is Positive or Negative


number=int(input("Enter a number: "))
test =lambda x: "Positive" if x>0 else "Negative"

res=test(number)
print(f"{number} is {res} ! ")