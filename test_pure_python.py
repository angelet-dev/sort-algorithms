from benchmarks import benchmark_runner_Python
import logging

# Importing of algorithms to test
# =============================================================
from algorithms.pure_python_algos import numba_merge_sort
from algorithms.pure_python_algos import merge_sort, bad_merge_sort, bubble_sort

# =============================================================

# If you want to see logs, change WARNING to INFO
logging.basicConfig(
    level=logging.INFO,
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
    iterations = 90  # Number of unique unsorted arrays to test
    num_workers = 3  # Number of parallel processes

# =============================================================

    benchmark_runner_Python(list_of_methods, N, iterations, num_workers)
