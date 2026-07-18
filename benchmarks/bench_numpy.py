import timeit
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np
import gc
from utils import form_results


def measure_single_sort(sort, array: list) -> float:
    temp_array = np.copy(array)
    standard = np.copy(array)
    standard.sort(kind="quicksort")

    gc.collect()

    execute_time = timeit.timeit(lambda: sort(temp_array), number=1)

    if not np.array_equal(temp_array, standard):
        logging.error(f"CRITICAL: {sort.__name__} FAILED TO SORT THE ARRAY!")
        raise AssertionError(f"Algorithm {sort.__name__} is broken!")
    logging.info(f"{sort.__name__} finished in {execute_time:.6f} sec")

    return execute_time


def benchmark_runner_NumPy(
    sort_func_list: list,
    array_size: int,
    iterations: int,
    num_workers: int,
    built_in_sort: str,
) -> None:

    builtin_sort_times = np.zeros(shape=iterations)
    list_of_times = np.zeros(shape = (len(sort_func_list), iterations))

    print("Start testing. It may take a lot of time...")
    # Generating dataset
    warm_up = np.zeros(shape=(num_workers,1), dtype=np.int64)
    all_unsorted_arrays = np.random.default_rng().integers(
        array_size * iterations, size=(iterations, array_size)
    )
    
    # Testing custom algorithms
    for i, sort_func in enumerate(sort_func_list):
        logging.info(
            f"--- Testing method: {sort_func.__name__} (N = {array_size}, {i + 1}/{len(sort_func_list)}) ---"
        )
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            run_test_with_method = partial(measure_single_sort, sort_func_list[i])
            
            list(executor.map(run_test_with_method, warm_up))
            
            list_of_times[i, :] = np.array(list(
                executor.map(run_test_with_method, all_unsorted_arrays)
            ))

    # Testing Python built-in sort
    logging.info(f"--- Testing NumPy built-in {built_in_sort} ---")
    for i, array in enumerate(all_unsorted_arrays):
        execute_time = timeit.timeit(
            lambda: array.sort(kind=built_in_sort), number=1
        )
        builtin_sort_times[i] = execute_time

    sort_tag = f"build-in NumPy {built_in_sort}"

    form_results(
        sort_func_list,
        list_of_times, 
        builtin_sort_times, 
        array_size,
        num_workers,
        iterations,
        sort_tag,
    )