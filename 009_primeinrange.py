import math

def prime(low, high):
    for num in range(low, high + 1):
        if num < 2:
            print(f"{num} is NOT a prime number")
            continue

        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is NOT a prime number")

prime(2, 10)
