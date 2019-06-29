import datetime
import random

bubble_stats =[]
stats = {}
def calc_run_time_stats(start, end):
    return end - start
          

def merge_sort_array(arr):
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid] 
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
          

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


def bubble_sort_array(arr):
    start_time =  timer()
    arr_len = len(arr)
    for i in range(arr_len): 
        for j in range(0, arr_len-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = timer()
    run_time = calc_run_time_stats(start_time, end_time)
    bubble_stats.append(run_time)

def timer():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    return current_time


#generate random array max_runs times with 500-max_right_val size
def fill_array(max_runs, max_right_val):
                              
    for i in range(max_runs):
        arr = []
        max_arr_len = random.randint(500, max_right_val)
        for j in range(max_arr_len):
            arr.append(random.randint(0, 1000))
        bubble_sort_array(arr)


def main():
    fill_array(3, 1500)
    print(bubble_stats)
    
main()
