def leap_year(year):
    flag="Non-Leap year"
    if year%4==0:
        flag="Leap year"
        if year%100==0:
            flag="Non-Leap year"
            if year%400==0:
                flag="Leap year"
    return flag


YEAR=int( input("Enter a year: "))
res=leap_year(YEAR)
print(f"{YEAR} is a {res}")