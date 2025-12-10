num = 8
ans = 0
rans = 0

for i in range(num + 1):
    ans = ans + i
    i = i - 1

print(f"using for loop {ans}")

fans = num * ((num + 1) / 2)
print(f"using nth sum formula prolly {fans}")

def recur(i):
    if i == 0:
        return 0
    else:
        return i + recur(i-1)

rans = recur(num)
print(f"using recursion {rans}")