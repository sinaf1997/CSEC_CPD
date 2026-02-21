shoes = list(map(int, input().split()))

unique_colors = set(shoes)
duplicates = len(shoes) - len(unique_colors)

print(duplicates)
