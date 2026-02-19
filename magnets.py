n = int(input())
previous = ""
groups = 0

for _ in range(n):
    current = input().strip()
    if current != previous:
        groups += 1
        previous = current

print(groups)
