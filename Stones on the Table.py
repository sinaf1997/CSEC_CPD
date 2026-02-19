n = int(input())
stones = input().strip()

remove_count = 0

for i in range(1, n):
    if stones[i] == stones[i - 1]:
        remove_count += 1

print(remove_count)
