def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact
def binomialCoeff_bruteForce(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))
def binomialCoeff_DP(n,k):
    c=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return c[n][k]
n=int(input("enter the value of n:"))
k=int(input("enter the value of k:"))
result_bruteForce=binomialCoeff_bruteForce(n,k)
result_DP=binomialCoeff_DP(n,k)
print(f"Binomail coefficient(Brute force):{result_bruteForce}")
print(f"Binomail coefficient(Dynamic programming):{result_DP}")
