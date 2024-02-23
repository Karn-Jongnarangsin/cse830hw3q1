import timeit
import matplotlib.pyplot as plt
import random
import numpy as np

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(algorithm, arr):
    start_time = timeit.default_timer()
    sorted_arr = algorithm(arr)
    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time

input_sizes = range(10, 200, 10)
num_iterations = 1000

merge_sort_accumulator = np.zeros(len(input_sizes))
insertion_sort_accumulator = np.zeros(len(input_sizes))

for _ in range(num_iterations):
    for j, n in enumerate(input_sizes):
        arr = [random.randint(1, 1000) for _ in range(n)]  # Generate random list of size n
    
        merge_sort_time = measure_time(merge_sort, arr.copy())
        merge_sort_accumulator[j] += merge_sort_time
        
        insertion_sort_time = measure_time(insertion_sort, arr.copy())
        insertion_sort_accumulator[j] += insertion_sort_time

avg_merge_sort_times = merge_sort_accumulator / num_iterations
avg_insertion_sort_times = insertion_sort_accumulator / num_iterations

plt.plot(input_sizes, avg_merge_sort_times, label='Merge Sort')
plt.plot(input_sizes, avg_insertion_sort_times, label='Insertion Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
