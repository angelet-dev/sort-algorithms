import logging
from typing import Literal
from benchmarks import benchmark_runner_NumPy

# Importing of algorithms to test
# =============================================================
from algorithms.numpy_base_algos import numba_merge_sort
from algorithms.numpy_base_algos import merge_sort, bad_merge_sort, bubble_sort

# =============================================================

# If you want to see logs, change WARNING to INFO
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s", 
    datefmt="%H:%M:%S",
    force=True,
)


if __name__ == "__main__":
   
# =============================================================
    # List of all algorithms to test
    list_of_methods = [numba_merge_sort, merge_sort, bad_merge_sort, bubble_sort]

    # Warning: Don't use a very large N and many iterations at the same time!

    N = 1000  # Size of the unsorted array
    iterations = 80  #  Number of unique unsorted arrays to test
    num_workers = 3  # Number of parallel processes
    built_in_sort: Literal["quicksort", "mergesort", "heapsort", "stable"] = "quicksort"  # NumPy built-in sort algorithm for comparison

# =============================================================

    benchmark_runner_NumPy(list_of_methods, N, iterations, num_workers, built_in_sort)
