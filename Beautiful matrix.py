row = 0
col = 0

for i in range(5):
    line = list(map(int, input().split()))
    for j in range(5):
        if line[j] == 1:
            row = i
            col = j


moves = abs(2 - row) + abs(2 - col)
print(moves)
