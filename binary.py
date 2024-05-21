import time
import matplotlib.pyplot as plt
# Function to run linear search multiple times and record results
def binarysearch(r):
    Results = []
    
    for i in range(r):
        Arr=[]
        N = int(input(" Enter the value of n"))
        for j in range(N):
            Arr.append(j)
        # print(Arr)
        Key = N-1
        # Repeat the search operation multiple times to amplify the time taken
        Repeat = 1
        Result = -1
        Start = time.time()
    
        for k in range(Repeat): 
            for i in range(N):
                l=0
                h=N-1
                while(l<=h):
                   mid=int((l+h)/2)
                   if Arr[mid] == Key:
                        Result = i
                        break
                   elif Arr[mid]<Key:
                        l=mid+1
                   else:
                        h=mid-1  
        End = time.time()
        if Result != -1:
            print(f"Key {Key} found at position {Result}")
        else:
            print (f"Key {Key} not found")

        time_taken =(End - Start)  
        print("time taken in micro seconds")
        print(time_taken)
        # Record number of elements and time taken
        Results.append((N,time_taken))
    return Results

def plot_results(results):
    n_values=[result[0] for result in results]
    times = [result[1] for result in results]
    plt.figure()
    plt.plot(n_values,times,'o-')
    plt.xlabel('Number of ele')
    plt.ylabel('Time taken in milli sec')
    plt.title('Linear search time complexity')
    plt.grid(True)
    plt.show()
# Main function
R = int (input("Enter the number of runs: "))
x=binarysearch(R)
print(x)
plot_results(x)

