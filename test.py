from bad_merge_sort import bed_merge_sort
from merge_sort import merge_sort
from buble_sort import buble_sort

import time
import random
import textwrap
import os
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np

COUNT_CORE = os.cpu_count()
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s", 
    datefmt="%H:%M:%S",
    force=True,
)

def test_sort_time(sort, array: list) -> float:
    temp_array = array.copy()
    standard = array.copy()
    standard.sort()

    start_time = time.time()
    sort(temp_array)
    
    end_time = time.time()
    if temp_array != standard:
        logging.error(f"CRITICAL: {sort.__name__} FAILED TO SORT THE ARRAY!")
        raise AssertionError(f"Algorithm {sort.__name__} is broken!")
    logging.info(f"{sort.__name__} finished in {end_time - start_time:.4f} sec")
    return end_time - start_time


if __name__ == "__main__":
    st_sort = []
    all_unsort_arrays = []

    # =============================================================
    list_of_methods = [buble_sort]
    
    # Don't use a very large N and many iterations at the same time!
    N = 10000
    iteration = 30 

    # ==============================================================

    list_of_times = [[] for _ in range(len(list_of_methods))]
    print("Start testing. It may take a lot of time...")
    for _ in range(iteration):
        all_unsort_arrays.append([random.random() * N * 10 for _ in range(N)])

    for i in range(len(list_of_methods)):
        logging.info(f"--- Testing method: {list_of_methods[i].__name__} (N = {N}) ---")
        with ProcessPoolExecutor(max_workers=COUNT_CORE) as executor:
            run_test_with_method = partial(test_sort_time, list_of_methods[i])
            list_of_times[i] = list(
                executor.map(run_test_with_method, all_unsort_arrays)
            )

    logging.info("--- Testing Python built-in sort() ---")
    for array in all_unsort_arrays:
        temp_array = array.copy()
        start_time = time.time()
        temp_array.sort()
        end_time = time.time()
        st_sort.append(end_time - start_time)

    results = textwrap.dedent("""
    =========================================================================
                                    RESULTS                  
    =========================================================================
    """).strip()
    print(results)

    sort_mean_time = np.mean(st_sort)

    for i in range(len(list_of_methods)):
        mean_time = np.mean(list_of_times[i])
        min_time = np.min(list_of_times[i])
        max_time = np.max(list_of_times[i])
        ratio = mean_time / sort_mean_time

        report = textwrap.dedent(f"""
        Name of sort algorithm:             {list_of_methods[i].__name__}
        Number of elements in array:        {N:,}
        Number of iterations:               {iteration}
        Mean time of sort:                  {mean_time:.6f} sec
        Min time of sort:                   {min_time:.6f} sec
        Max time of sort:                   {max_time:.6f} sec
        In comparison with built-in:        {ratio:.2f}x slower
        =========================================================================
        """).strip()
        print(report)