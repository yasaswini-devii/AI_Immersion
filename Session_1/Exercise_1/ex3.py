def gcd_lcm(a, b):
    maxi, mini = max(a, b), min(a, b)
    while mini != 0:
        maxi, mini = mini, maxi % mini
    gcd = maxi
    lcm = abs(a * b) // gcd
    return gcd, lcm

print(gcd_lcm(12, 18))  
print(gcd_lcm(15, 27))
