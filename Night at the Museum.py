s = input().strip()
current = 'a'
total = 0

for ch in s:   
    diff = abs(ord(ch) - ord(current))   
    total += min(diff, 26 - diff)
    current = ch
print(total)
