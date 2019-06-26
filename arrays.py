import datetime
import random

stats = {}
def calc_run_time_stats(start, end, length, algorithm):
    #do stuff with algorithm name
    run_time = end - start
    data_pair = {length: run_time}
    if (algorithm == 'bubble_sort'):
        if ('bubble_sort' not in stats):
            stats['bubble_sort']['runtime'] = run_time
    print(stats)
    return end - start


def bubble_sort_array(arr):
    start_time =  timer()
    arr_len = len(arr)
    for i in range(arr_len): 
        for j in range(0, arr_len-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = timer()
    run_time = calc_run_time_stats(start_time, end_time, arr_len, 'bubble_sort')
    print('')
    print('Bubble Sort:',run_time)


def timer():
    current_time = datetime.datetime.now()
    return current_time


def fill_array(max_runs, max_right_val):
                              
    for i in range(max_runs):
        arr = []
        max_arr_len = random.randint(500, max_right_val)
        for j in range(max_arr_len):
            arr.append(random.randint(0, 1000))
        bubble_sort_array(arr)


def main():
    fill_array(30, 1500)
    
    
main()
