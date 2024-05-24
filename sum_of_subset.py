def sum_of_subsets(s,k,r):
    global count,x,w,d,i
    x[k]=1
    if s+w[k]==d:
        print("\n subset %d ="%(count+1),end="")
        for i in range(k+1):
            if x[i]:
                print("%d "%w[i],end="")
    elif s+w[k]+w[k]<=d:
        sum_of_subsets(s+w[k],k+1,r-w[k])
    if s+r-w[k]>=d and s+w[k]<=d:   
        x[k]=0
        sum_of_subsets(s,k+1,r-w[k])
if __name__=="__main__":
    w=[0]*10
    x=[0]*10
    count=0
    i=0
    n=int(input("enter no ele:"))
    print("enter ele in ascending order:")
    for i in range(n):
        w[i]=int(input())
    d=int(input("enter the sum"))
    sum=0 
    for i in range(n):
        x[i]=0
        sum+=w[i]
    if sum<d or w[0]>d:
        print("\n no of subset possible\n")
    else:
        sum_of_subsets(0,0,sum)