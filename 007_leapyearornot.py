
def leapYear(params):
    if params % 400 == 0 or (params %4 ==0 and params % 100 != 0):
        return (f"{params} is Leap year")
    else:
        return (f" {params} is not Leap year")
print(leapYear(2020))

year = 2020
answer = "Leap year" if year % 400 == 0 or (year %4 ==0 and year % 100 != 0) else "Not leap year"
print(f" {year} is {answer} ")

