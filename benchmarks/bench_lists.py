import timeit
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np
import gc
from utils import form_results, save_results_to_file


def measure_single_sort(sort, array: list, baseline: list) -> float:
    temp_array = array.copy()

    gc.collect()

    execute_time = timeit.timeit(lambda: sort(temp_array), number=1)

    if not np.array_equal(temp_array, baseline):
        logging.error(f"CRITICAL: {sort.__name__} FAILED TO SORT THE ARRAY!")
        raise AssertionError(f"Algorithm {sort.__name__} is broken!")
    logging.info(f"{sort.__name__} finished in {execute_time:.6f} sec")

    return execute_time


def benchmark_runner_Python(
    sort_func_list: list,
    array_size: int,
    iterations: int,
    num_workers: int,
    DTYPE: str,
    save_to_file: bool,
) -> None:

    builtin_sort_times = np.zeros(shape=iterations)
    list_of_times = np.zeros(shape=(len(sort_func_list), iterations))

    all_unsorted_arrays = []

    print("Start testing. It may take a lot of time...")
    
    if DTYPE == "int":
        warm_up = [[int(1)] for _ in range(num_workers)]
    elif DTYPE == "float":
        warm_up = [[float(1)] for _ in range(num_workers)]

    partial_list = [
        partial(measure_single_sort, sort_func_list[i])
        for i in range(len(sort_func_list))
    ]

    
    step = min(iterations, num_workers)
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for func in partial_list:
            list(executor.map(func, warm_up, warm_up))

        for j in range(step, iterations + step, step):
            number_arrays = step if iterations - j >= 0 else iterations % step
            if DTYPE == "int":
                gen_array = np.random.default_rng().integers(
                    low=-array_size, high=array_size, size=(number_arrays, array_size)
                )
            elif DTYPE == "float":
                gen_array = np.random.default_rng().uniform(
                    low=-1.0 * array_size,
                    high=1.0 * array_size,
                    size=(number_arrays, array_size),
                )
            all_unsorted_arrays = gen_array.tolist()

            # Testing Python built-in sort
            baseline = all_unsorted_arrays.copy()
            logging.info(f"--- Testing Python built-in sort() ({j - step + number_arrays}/{iterations})---")
            for i in range(len(baseline)):
                execute_time = timeit.timeit(lambda: baseline[i].sort(), number=1)
                builtin_sort_times[i + j - step] = execute_time
                logging.info(
                    f"Python built-in sort() finished in {builtin_sort_times[i + j - step]:.6f} sec"
                )

            # Testing custom algorithms
            for i, sort_func in enumerate(sort_func_list):
                logging.info(
                    f"--- Testing method: {sort_func.__name__} (N = {array_size}, {i + 1}/{len(sort_func_list)}, {j - step + number_arrays}/{iterations}) ---"
                )

                list_of_times[i, j - step : j] = np.array(
                    list(executor.map(partial_list[i], all_unsorted_arrays, baseline))
                )



    sort_tag = "built-in Tim Sort"
    text = form_results(
        sort_func_list,
        list_of_times,
        builtin_sort_times,
        array_size,
        num_workers,
        iterations,
        sort_tag,
        DTYPE,
    )
    print(text)

    save_results_to_file(text, save_to_file, "bench_list")
