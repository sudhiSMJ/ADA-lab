import time
import matplotlib.pyplot as plt
# Function to run linear search multiple times and record results
def linearsearch(r):
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
                if Arr[i] == Key:
                    Result = i
                    break
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
x=linearsearch(R)
print(x)
plot_results(x)

