import sys

def minkey(key,mstSet,n):
    min_value=sys.maxsize
    for v in range(n):
        if mstSet[v]==False and key[v]<min_value:
            min_value=key[v]
            min_index=v
    return min_index

def printMST(parent,c,n):
    totalWeight=0
    print("edge  weight")
    for i in range(1,n):
        print(str(parent[i]+1)+ "_"+str(i+1)+" "+str(c[i][parent[i]]))
        totalWeight +=c[i][parent[i]]
    return totalWeight

def primMST(c,n):  
    parent=[None]*n
    key=[sys.maxsize]*n
    mstSet=[False]*n
    key[0]=0
    parent[0]=-1
    for count in range(n):
        u=minkey(key,mstSet,n)
        mstSet[u]=True
        for v in range(n):
            if c[u][v]>0 and mstSet[v]==False and c[u][v]<key[v]:
                parent[v]=u
                key[v]=c[u][v]
        totalWeight=printMST(parent,c,n)
    print("total cost of the minimum spamming tree:"+str(totalWeight))

n=int(input("enter the number of vertices:"))
c=[]
print("enter the cost adjacency matrix:")
for i in range(n):
    c.append(list(map(int,input().split())))
primMST(c,n)