import timeit
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import logging
import numpy as np
import gc
from utils import form_results, save_results_to_file


def measure_single_sort(sort, array: np.array, baseline: np.array) -> float:
    temp_array = np.copy(array)
    gc.collect()

    execute_time = timeit.timeit(lambda: sort(temp_array), number=1)

    if not np.array_equal(temp_array, baseline):
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
    DTYPE: str,
    save_to_file: bool,
) -> None:

    builtin_sort_times = np.zeros(shape=iterations)
    list_of_times = np.zeros(shape=(len(sort_func_list), iterations))

    print("Start testing. It may take a lot of time...")
    if DTYPE == "int64":
        warm_up = np.zeros(shape=(num_workers, 1), dtype=np.int64)
    elif DTYPE == "float64":
        warm_up = np.zeros(shape=(num_workers, 1), dtype=np.float64)

    partial_list = [
        partial(measure_single_sort, sort_func_list[i])
        for i in range(len(sort_func_list))
    ]

    # Testing custom algorithms
    step = min(iterations, num_workers)
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for func in partial_list:
            list(executor.map(func, warm_up, warm_up))

        for j in range(step, iterations + step, step):
            number_arrays = step if iterations - j >= 0 else iterations % step

            if DTYPE == "int64":
                all_unsorted_arrays = np.random.default_rng().integers(
                    low=-array_size, high=array_size, size=(number_arrays, array_size)
                )
            elif DTYPE == "float64":
                all_unsorted_arrays = np.random.default_rng().uniform(
                    low=-1.0 * array_size,
                    high=array_size,
                    size=(number_arrays, array_size),
                )
            
            # Testing Python built-in sort
            logging.info(f"--- Testing NumPy built-in {built_in_sort} ---")
            baseline = np.copy(all_unsorted_arrays)
            for i, _ in enumerate(baseline):
                execute_time = timeit.timeit(
                    lambda: baseline[i].sort(kind=built_in_sort), number=1
                )
                builtin_sort_times[i + j - step] = execute_time
                logging.info(
                    f"NumPy built-in {built_in_sort} finished in {builtin_sort_times[i + j - step]:.6f} sec ({j - step + number_arrays}/{iterations})"
                )

            # Testing Python coustom sort
            for i, sort_func in enumerate(sort_func_list):
                logging.info(
                    f"--- Testing method: {sort_func.__name__} (N = {array_size}, {i + 1}/{len(sort_func_list)}, {j - step + number_arrays}/{iterations})) ---"
                )

                list_of_times[i, j - step : j] = np.array(
                    list(executor.map(partial_list[i], all_unsorted_arrays, baseline))
                )


    sort_tag = f"build-in NumPy {built_in_sort}"

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

    save_results_to_file(text, save_to_file, "bench_numpy")
