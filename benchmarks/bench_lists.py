import timeit
import random
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np
import gc
from utils import form_results, save_results_to_file

def test_sort_time(sort, array: list) -> float:
    temp_array = array.copy()
    standard = array.copy()
    standard.sort()

    gc.collect()

    execute_time = timeit.timeit(lambda: sort(temp_array), number=1)

    if not np.array_equal(temp_array, standard):
        logging.error(f"CRITICAL: {sort.__name__} FAILED TO SORT THE ARRAY!")
        raise AssertionError(f"Algorithm {sort.__name__} is broken!")
    logging.info(f"{sort.__name__} finished in {execute_time:.6f} sec")

    return execute_time


def benchmark_runner_Python(
    sort_func_list: list, array_size: int, iterations: int, num_workers: int
) -> None:

    builtin_sort_times = np.zeros(shape=iterations)
    list_of_times = np.zeros(shape=(len(sort_func_list), iterations))

    all_unsorted_arrays = []

    print("Start testing. It may take a lot of time...")
    # Generating dataset
    warm_up = [[1.0] for _ in range(num_workers)]
    for _ in range(iterations):
        all_unsorted_arrays.append(
            [random.uniform(-1, 1) * array_size for _ in range(array_size)]
        )

    # Testing custom algorithms
    for i, sort_func in enumerate(sort_func_list):
        logging.info(
            f"--- Testing method: {sort_func.__name__} (N = {array_size}, {i + 1}/{len(sort_func_list)}) ---"
        )
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            run_test_with_method = partial(test_sort_time, sort_func_list[i])

            list(executor.map(run_test_with_method, warm_up))

            list_of_times[i, :] = np.array(list(
                executor.map(run_test_with_method, all_unsorted_arrays)
            ))

    # Testing Python built-in sort
    logging.info("--- Testing Python built-in sort() ---")
    for i, array in enumerate(all_unsorted_arrays):
        execute_time = timeit.timeit(lambda: array.sort(), number=1)
        builtin_sort_times[i] = execute_time


    sort_tag = "built-in Tim Sort"
    text = form_results(sort_func_list, list_of_times, builtin_sort_times, array_size, num_workers, iterations, sort_tag)
    print(text)
    
    save_results_to_file(text, "bench_list")