a1, a2, a3, a4 = map(int, input().split())
s = input().strip()

total = 0
for ch in s:
    if ch == '1':
        total += a1
    elif ch == '2':
        total += a2
    elif ch == '3':
        total += a3
    elif ch == '4':
        total += a4

print(total)
