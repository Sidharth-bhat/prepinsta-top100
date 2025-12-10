num1=2
num2=5

def func1(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
ans1=func1(num1,num2)
print(f"Using IF-ELSE statement method : {ans1} ")

def func2(num1,num2):
    return num1 if num1>num2 else num2
ans2=func2(num1,num2)
print(f"Using TERNARY operator : {ans2} ")

def func3(num1,num2):
    return max(num1,num2)
ans3=func3(num1,num2)
print(f"Using in-built max function method : {ans3} ")