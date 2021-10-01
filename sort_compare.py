import random
import time
    

    

def get_me_random_list(n):
    a_list = list(range(n+1))
    random.shuffle(a_list)
    return(a_list)


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:

            a_list[position] = a_list[position - 1]
            position = position - 1

            a_list[position] = current_value

    end = time.time()

    return end - start


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time()

    return end - start


def gap_insertion_sort(a_list, start, gap):
    start_time = time.time()
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

    end = time.time()

    return end - start_time
    

    

def python_sort(a_list):
    start = time.time()

    sorted(a_list)

    end = time.time()

    return end - start
    


def main(n):
    total_runtime = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        time = insertion_sort(a_list)
        total_runtime += t1
    avg_runtime = total_runtime/100
    print("Insertion Sort result took {:10.7f} seconds to run, on average.".format(avg_runtime))
    

    total_runtime = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        time = shell_sort(a_list)
        total_runtime += time
    avg_runtime = total_runtime/100
    

    print("Shell Sort result took {:10.7f} seconds to run, on average.".format(avg_runtime))
    

    total_runtime = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        time = python_sort(a_list)
        total_runtime += time
    avg_runtime = total_runtime/100
    

    print("Python Sort result took {:10.7f} seconds to run, on average. \n".format(avg_runtime))
    

    

if __name__ == "__main__":
    L = [500, 1000, 5000]
    counter = 0
    for i in L:
        print("For list size: {}".format(L[counter]))
        main(L[counter])
        counter += 1

    
        
        
