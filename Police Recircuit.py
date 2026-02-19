n = int(input())
events = list(map(int, input().split()))

available = 0
unresolved = 0

for x in events:
    if x > 0:
        available += x
    else:  # x == -1
        if available > 0:
            available -= 1
        else:
            unresolved += 1

print(unresolved)
