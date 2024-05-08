def power_bruteforce(a,n):
    result = 1
    for i in range(n):
        result *= a
    return result
def power_dandc(a,n):
    if n==0:
        return 1
    elif n%2==0:
        return power_dandc(a*a,n//2)
    else:
        return a*  power_dandc(a*a,n//2)
a, n = map(int, input("Enter the input for a and n: ").split())
result_b=power_bruteforce(a,n)
result_dandc=power_dandc(a,n)
print("result using brute force:",result_b)
print("result using dandc:",result_dandc)