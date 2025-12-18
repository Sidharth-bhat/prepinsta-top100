num=5
def prime(num):
    count=0
    for i in range(2,num):
        if num%i==0:
            count=1
            break
    if count==1:
        print(f"The {num} is NOT prime number ")
    else:
        print(f"The {num} is a prime number ")
prime(num)


def primerec(num,i=2):
    if num == i :
        return True
    if  num%i ==0:
        return False
    return primerec(num,i+1)
if primerec(num,i=2) is True:
        print(f"The {num} is  prime number ")
else:
        print(f"The {num} is NOT a prime number")