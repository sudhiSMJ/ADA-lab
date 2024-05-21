import timeit
import random
import matplotlib.pyplot as plt

def Input_array(arry,n):
    for i in range(0,n):
        ele=random.randrange(1,1000000)
        array.append(ele)
def partition(array,low,high):
    i=(low-1)
    pivot=array[high]
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)
def quicksort(array,low,high):
    if(low<high):
        pi=partition(array,low,high)
        quicksort(array,low,pi-1) 
        quicksort(array,pi+1,high)
N=[]
CPU=[]
trail=int(input("enter the no. of trails:"))
for i in range(0,trail):
    array=[]
    print("--> trail no",i+1)
    n=int(input(" enter the no. of elelments")) 
    Input_array(array,n)
    start=timeit.default_timer()
    quicksort(array,0,n-1)
    times=timeit.default_timer()-start
    print("sorted array")
    print(array)
    N.append(n)
    CPU.append(round(float(times)*10000,2))
print("N CPU")
for t in range(0,trail):
    print(N[t],CPU[t])
plt.plot(N,CPU)    
plt.scatter(N,CPU,color="red",marker="*",s=50) 
plt.xlabel("N")
plt.ylabel("CPU")
plt.show()       

            