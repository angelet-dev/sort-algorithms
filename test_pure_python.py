from benchmarks import benchmark_runner_Python
import logging
from typing import Literal

# Importing of algorithms to test
# =============================================================
from algorithms.pure_python_algos import numba_merge_sort
from algorithms.pure_python_algos import merge_sort, bad_merge_sort, bubble_sort

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

    N = 5000  # Size of the unsorted array
    iterations = 10  # Number of unique unsorted arrays to test
    num_workers = 4  # Number of parallel processes
    save_report = False  # True - save report of benchmark to .txt | False - pass
    DTYPE: Literal["int", "float"] = "int"  # Data type of elements in array

    # =============================================================

    benchmark_runner_Python(
        list_of_methods, N, iterations, num_workers, DTYPE, save_report
    )
