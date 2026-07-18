from bad_merge_sort import bad_merge_sort # in-place merge sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort

import logging
from benchmark import test_list_sorts

# If you want to see logs, change INFO to WARNING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s", 
    datefmt="%H:%M:%S",
    force=True,
)

if __name__ == "__main__":
   
# =============================================================
    # List of all algorithms to test
    list_of_methods = [merge_sort, bad_merge_sort, bubble_sort]

    # Warning: Don't use a very large N and many iterations at the same time!

    N = 1000  # Size of the unsorted array
    iterations = 50  # Number of unsorted arrays to test
    num_workers = 3  # Number of parallel threads/processes
# =============================================================

    test_list_sorts(list_of_methods, N, iterations, num_workers)
