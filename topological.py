
def main():
    n=int(input("enter the no of vertices"))
    count=0
    c=[[0 for _ in range(n)]for _ in range(n)]
    indeg=[0]*n
    flag=[0]*n
    i,j,k=0,0,0
    print("enetr the  cost matrix row by row")
    for i in range(n):
        row=input().split()
        for j in range(n):
            c[i][j]=int(row[j])
    for i in range(n):
        for j in range(n):
            indeg[i]+=c[j][i]
    print("the topological order is:")
    while count < n:
        for k in range(n):
            if indeg[k]==0 and flag[k]==0:
                print(f"{k+1:3}",end="")
                flag[k]=1
                count+=1
                for i in range(n):
                    if c[k][i]==1:
                        indeg[i]-=1
    return 0

main()






    







    
