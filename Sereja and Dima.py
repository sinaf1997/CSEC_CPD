n = int(input())
arr = list(map(int, input().split()))

sereja = 0
dima = 0
turn = 0  

left = 0
right = n - 1

while left <= right:
    if arr[left] > arr[right]:
        chosen = arr[left]
        left += 1
    else:
        chosen = arr[right]
        right -= 1

    if turn == 0:
        sereja += chosen
        turn = 1
    else:
        dima += chosen
        turn = 0

print(sereja, dima)
