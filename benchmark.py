import timeit
import random
import textwrap
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np
import gc


def test_sort_time(sort, array: list) -> float:
    temp_array = array.copy()
    standard = array.copy()
    standard.sort()

    execute_time = timeit.timeit(lambda: sort(temp_array), number=1)

    if not np.array_equal(temp_array, standard):
        logging.error(f"CRITICAL: {sort.__name__} FAILED TO SORT THE ARRAY!")
        raise AssertionError(f"Algorithm {sort.__name__} is broken!")
    logging.info(f"{sort.__name__} finished in {execute_time:.4f} sec")

    gc.collect()

    return execute_time


def test_list_sorts(
    sort_func_list: list, array_size: int, iterations: int, num_workers: int
) -> None:

    builtin_sort_times = []
    all_unsorted_arrays = []
    list_of_times = [[] for _ in range(len(sort_func_list))]

    print("Start testing. It may take a lot of time...")
    # Generating dataset
    for _ in range(iterations):
        all_unsorted_arrays.append(
            [random.uniform(-1, 1) * array_size for _ in range(array_size)]
        )

    # Testing custom algorithms
    for i, sort_func in enumerate(sort_func_list):
        logging.info(f"--- Testing method: {sort_func.__name__} (N = {array_size}, {i+1}/{len(sort_func_list)}) ---")
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            run_test_with_method = partial(test_sort_time, sort_func_list[i])
            list_of_times[i] = list(
                executor.map(run_test_with_method, all_unsorted_arrays)
            )

    # Testing Python built-in sort
    logging.info("--- Testing Python built-in sort() ---")
    for array in all_unsorted_arrays:
        temp_array = array.copy()
        execute_time = timeit.timeit(lambda: temp_array.sort(), number=1)
        builtin_sort_times.append(execute_time)

    results = textwrap.dedent("""
    =========================================================================
                                    RESULTS                  
    =========================================================================
    """).strip()
    print(results)

    builtin_mean_time = np.mean(builtin_sort_times)

    for i in range(len(sort_func_list)):
        mean_time = np.mean(list_of_times[i])
        min_time = np.min(list_of_times[i])
        max_time = np.max(list_of_times[i])
        ratio = mean_time / builtin_mean_time

        pure_core_time = sum(list_of_times[i]) / num_workers

        report = textwrap.dedent(f"""
        Name of sort algorithm:             {sort_func_list[i].__name__}
        Number of elements in array:        {array_size:,}
        Number of iterations:               {iterations}
        Mean time of sort:                  {mean_time:.6f} sec
        Min time of sort:                   {min_time:.6f} sec
        Max time of sort:                   {max_time:.6f} sec
        Pure CPU time per core:             {pure_core_time:.4f} sec
        Number of workers (cores):          {num_workers} 
        In comparison with built-in:        {ratio:.2f}x slower
        =========================================================================
        """).strip()
        print(report)
