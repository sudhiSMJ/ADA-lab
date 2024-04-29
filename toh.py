import matplotlib.pyplot as plt

def toh(n,source,temp,dest):
    global count
    if n>0:
        toh(n-1,source,dest,temp)
        print(f"move disk {n} {source}->{dest}")
        count +=1
        toh(n-1,temp,source,dest)
def plot_results(results):
    n_values=[result[0] for result in arr]
    times = [result[1] for result in arr]
    plt.figure()
    plt.plot(n_values,times,'o-')
    plt.xlabel('no.of disks')
    plt.ylabel('moves')
    plt.title(' tover of honoi')
    plt.grid(True)
    plt.show()
source="S"
temp="T"
dest="D"
arr=[]
R = int (input("Enter the number of runs: ")) 
for i in range(R):     
    count=0
    n=int(input("enter the number of disks:"))
    print("the sequence is:")
    toh(n,source,temp,dest)
    arr.append((n,count))
    print("the no. of moves:",count)
print(arr)
plot_results(arr)


