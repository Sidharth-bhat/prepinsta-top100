num1=2
num2=5
ans=0
for i in range(num1,num2+1):
    ans=ans+i
print(f"using BruteForce : {ans}")

ans2 =int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(f"Using formula : {ans2} ")

def recur(num1,num2):
    if num1 > num2:
        return 0
    else:
        return num1 + recur(num1+1,num2)
        
    

ans3=recur(2,5)
print(f"using recursion : {ans3} ")