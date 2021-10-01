import random
import time


def get_me_random_list(n):
    array = list(range(n))
    random.shuffle(array)
    return(array)


def sequential_search(array, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()
    return found, end - start


def ordered_sequential_search(array, item):
    start = time.time()
    pos = 0
    found = False
    stop = False


    while pos < len(array) and not found and not stop:
        if array[pos] == item:
            found = True
        else:
            if array[pos] > item:
                stop = True
            else:
                pos += 1
    end = time.time()
    return found, end - start




def binary_search_iterative(array, item):
    start = time.time()
    first = 0
    last = len(array) - 1
    found = False


    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end - start




def binary_search_recursive(array, item):
    start = time.time()
    if len(array) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(array) // 2
        if array[midpoint] == item:
            end = time.time()
            return True, end - start
        else:
            if item < array[midpoint]:
                return binary_search_recursive(array[:midpoint], item)
            else:
                return binary_search_recursive(array[midpoint + 1:], item)




def main(n, item):

    total_runtime = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        a1, time = sequential_search(b_list, item)
        total_runtime += time
    avg_runtime = total_runtime/100
    print("Sequential Search took {:10.7f} ".format(avg_runtime) + "seconds to run, on average.")


    total_runtime = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        b_list.sort()
        a2, time = ordered_sequential_search(b_list, item)
        total_runtime += time
    avg_runtime = total_runtime/100
    print("Ordered Sequential Search took {:10.7f} ".format(avg_runtime) + "seconds to run, on average.")


    total_runtime = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        sorted(b_list)
        a3, time = binary_search_iterative(b_list, item)
        total_runtime += time
    avg_runtime = total_runtime/100
    print("Binary Search Iterative took {:10.7f} ".format(avg_runtime) + "seconds to run, on average.")


    total_runtime = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        b_list.sort()
        a4, time = binary_search_recursive(b_list, item)
        total_runtime += time
    avg_runtime = total_runtime/100
    print("Binary Search Recursive took {:10.7f} ".format(avg_runtime) + "seconds to run, on average. \n")




if __name__ == "__main__":
    L = [500, 1000, 10000]
    counter = 0
    for i in L:
        print("For list size: {}".format(L[counter]))
        main(L[counter], -1)
        counter += 1

   
    
        
        
   
