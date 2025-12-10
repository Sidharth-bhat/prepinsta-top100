num1 = 23
num2 = 10
num3 = 50

def greatest_if(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

ans1 = greatest_if(num1, num2, num3)
print(f"Using if-elif method : {ans1}")

def greatest_nested(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

ans2 = greatest_nested(num1, num2, num3)
print(f"Using nested method  : {ans2}")

def greatest_max(a, b, c):
    return max(a, b, c)

ans3 = greatest_max(num1, num2, num3)
print(f"Using max() method    : {ans3}")
