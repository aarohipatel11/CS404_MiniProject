import random
import time
from typing import List

#credit to chatGPT for coding assistance

#generates a list of random integers of the given size
def gen_random_list(list_size: int) -> List[int]:
    return [random.randint(0, 1000000) for _ in range(list_size)]


#sorts given list, and returns runtime of the sort
def bubble_sort(list_to_sort:List[int]) -> float:
    start_time = time.time()
    n = len(list_to_sort)
    for i in range(n):
        # Track if any swap happens in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if elements are in wrong order
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                swapped = True
        # If no swaps happened, the array is already sorted
        if not swapped:
            break
    end_time = time.time()
    return (end_time - start_time)


def main() -> None: 
    size_of_lists:int = [10, 100, 1000, 10000, 100000, 1000000]
    for size in size_of_lists:
        temp_list = gen_random_list(size)
        run_time = bubble_sort(temp_list)
        print("For a list of size %s, runtime of bubble sort was %f", size, run_time)


if __name__ == '__main__':
    main()