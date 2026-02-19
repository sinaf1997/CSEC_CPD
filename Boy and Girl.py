username = input().strip()
distinct_letters = set(username)

if len(distinct_letters) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
