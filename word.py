word = input().strip()

lower_count = sum(1 for ch in word if ch.islower())
upper_count = sum(1 for ch in word if ch.isupper())

if lower_count >= upper_count:
    print(word.lower())
else:
    print(word.upper())
