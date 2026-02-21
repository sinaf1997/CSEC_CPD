import math
y, w = map(int, input().split())
m = max(y, w)
numerator = 6 - m + 1
denominator = 6
g = math.gcd(numerator, denominator)
print(f"{numerator//g}/{denominator//g}")
