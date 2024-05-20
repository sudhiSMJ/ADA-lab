import timeit
import random
import matplotlib.pyplot as plt
def Input(Array,n):
    for i in range(0,n):
        ele=random.randrange(1,1000000)
        Array.append(ele)
def selection_sort(Array,size):
    for ind in range(size):
        min_index=ind
        for j in range(ind+1,size):
            if Array[j]<Array[min_index]:
                min_index=j
        (Array[ind],Array[min_index])=(Array[min_index],Array[ind])
N=[ ]
CPU=[ ]
trail=int(input("enter no of trails:"))
for t in range(0,trail):
    Array=[]
    print("trail no:",t+1)
    n=int(input("enter no of elei"))
    Input(Array,n)
    start=timeit.default_timer()
    selection_sort(Array,n)
    times=timeit.default_timer()-start
    print("sorted Array:")
    print(Array)
    N.append(n)
    CPU.append(round(float(times)*10,2))
    print("N CPU")

for t in range (0,trail):
    print(N[t],CPU[t])

plt.plot(N,CPU)
plt.scatter(N,CPU,color="red",marker='*',s=50)
plt.xlabel("array sizeN")
plt.ylabel("cpu processing time")
plt.title("selection sort time efficiency")
plt.show()

