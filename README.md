# 🚀 sort-algorithms

**sort-algorithms is a benchmark framework and future library containing my implementations of various sorting algorithms.**

---
## 📦 What does it contain right now?

* **`merge sort`**: ⚡️ my implementation of the classic merge sort algorithm.
* **`numba_merge_sort`**: 🏎️ JIT compiled merge sort for extreme performance.
* **`bad_merge_sort`**: 🐢 my implementation of the core merge sort idea without creating additional arrays.
* **`bubble sort`**: 🐌 included strictly for performance comparison with the bad merge sort.
* **`bench_lists.py`**: Contains all the necessary functions for isolating benchmarks and managing multiprocessing for Python list-based sorting algorithms. 
* **`bench_numpy.py`**: The same as `bench_lists.py`, but designed for NumPy array-based sorting algorithms.
* **`results_output.py`**: Contains formatting functions for generating clean reports.
* **`test_numpy.py`**: 🧪 The main execution script to configure dataset parameters and run tests for NumPy-based algorithms.
* **`test_pure_python.py`**: 🧪 The same as `test_numpy.py`, but tailored for Python list-based algorithms.
---

## 🧠 Technical Highlights & Architecture

To ensure high accuracy and deep hardware analysis, the benchmarking framework implements the following:
* **Multiprocessing**: Utilizes `ProcessPoolExecutor` from Python's built-in `concurrent.futures` module to bypass the GIL and utilize multiple CPU cores.
* **Precision Timing**: Sorting duration is measured using the `timeit` module for microsecond-level accuracy.
* **Isolated Environment**: At the end of each test iteration, an explicit garbage collection (`gc.collect()`) is triggered. This purges the heap, prevents memory accumulation, and eliminates cache noise for subsequent runs.
* **Automated Logging**: All benchmark results are automatically saved into the `results/` directory as a `.txt` file for future analysis.
---

## 📊 Output Examples (test.py)

* **Example 1: Running `test_numpy.py`** 🏎️

    Parameters:
    ```python
    # List of all algorithms to test
    list_of_methods = [numba_merge_sort]

    N = 10000000  # Size of the unsorted array
    iterations = 9  #  Number of unique unsorted arrays to test
    num_workers = 3  # Number of parallel processes
    built_in_sort: Literal["quicksort", "mergesort", "heapsort", "stable"] = "quicksort"  # NumPy built-in sort algorithm for comparison

    ```
    Output:

    ```bash
   =========================================================================
                                RESULTS                  
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        10,000,000
    Number of iterations:               9
    Mean time of sort:                  1.498044 sec
    Min time of sort:                   1.482607 sec
    Max time of sort:                   1.517019 sec
    Pure CPU time per core:             4.4941 sec
    Number of workers (cores):          3 
    In comparison with build-in NumPy quicksort: 12.37x slower
    =========================================================================
    ```

* **Example 2: Testing and comparing multiple algorithms in `test_numpy.py`** 

    Parameters:
    ```python
    list_of_methods = [numba_merge_sort, merge_sort, bad_merge_sort, bubble_sort]

    N = 5000  
    iterations = 90  
    num_workers = 3  
    built_in_sort: Literal["quicksort", "mergesort", "heapsort", "stable"] = "quicksort"  
    ```

    Output:
    ```bash
    =========================================================================
                                    RESULTS                  
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        5,000
    Number of iterations:               90
    Mean time of sort:                  0.000608 sec
    Min time of sort:                   0.000425 sec
    Max time of sort:                   0.000986 sec
    Pure CPU time per core:             0.0182 sec
    Number of workers (cores):          3 
    In comparison with build-in NumPy quicksort: 14.78x slower
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        5,000
    Number of iterations:               90
    Mean time of sort:                  0.030085 sec
    Min time of sort:                   0.026490 sec
    Max time of sort:                   0.053948 sec
    Pure CPU time per core:             0.9025 sec
    Number of workers (cores):          3 
    In comparison with build-in NumPy quicksort: 731.75x slower
    =========================================================================
    Name of sort algorithm:             bad_merge_sort
    Number of elements in array:        5,000
    Number of iterations:               90
    Mean time of sort:                  2.629360 sec
    Min time of sort:                   2.155707 sec
    Max time of sort:                   3.044143 sec
    Pure CPU time per core:             78.8808 sec
    Number of workers (cores):          3 
    In comparison with build-in NumPy quicksort: 63954.05x slower
    =========================================================================
    Name of sort algorithm:             bubble_sort
    Number of elements in array:        5,000
    Number of iterations:               90
    Mean time of sort:                  8.450224 sec
    Min time of sort:                   7.304895 sec
    Max time of sort:                   9.049136 sec
    Pure CPU time per core:             253.5067 sec
    Number of workers (cores):          3 
    In comparison with build-in NumPy quicksort: 205535.22x slower
    =========================================================================
    ```

* **Example 3: Running `test_pure_python.py`** 

    Parameters:
    ```python
    # List of all algorithms to test
    list_of_methods = [numba_merge_sort]

    N = 10000000  # Size of the unsorted array
    iterations = 9  # Number of unique unsorted arrays to test
    num_workers = 3  # Number of parallel processes
    ```

    Output:
    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        10,000,000
    Number of iterations:               9
    Mean time of sort:                  12.974758 sec
    Min time of sort:                   11.623023 sec
    Max time of sort:                   13.868731 sec
    Pure CPU time per core:             38.9243 sec
    Number of workers (cores):          3 
    In comparison with built-in Tim Sort: 3.65x slower
    =========================================================================
    ```

* **Example 4:  Testing and comparing all sorts in `test_pure_python.py`** 

    Parameters:
    ```python
    list_of_methods = [numba_merge_sort, merge_sort, bad_merge_sort, bubble_sort]

    N = 1000  
    iterations = 90  
    num_workers = 3 

    ```

    Output:
    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.001118 sec
    Min time of sort:                   0.000913 sec
    Max time of sort:                   0.001721 sec
    Pure CPU time per core:             0.0335 sec
    Number of workers (cores):          3 
    In comparison with built-in Tim Sort: 12.83x slower
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.001562 sec
    Min time of sort:                   0.001148 sec
    Max time of sort:                   0.002211 sec
    Pure CPU time per core:             0.0469 sec
    Number of workers (cores):          3 
    In comparison with built-in Tim Sort: 17.93x slower
    =========================================================================
    Name of sort algorithm:             bad_merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.028371 sec
    Min time of sort:                   0.024737 sec
    Max time of sort:                   0.032691 sec
    Pure CPU time per core:             0.8511 sec
    Number of workers (cores):          3 
    In comparison with built-in Tim Sort: 325.70x slower
    =========================================================================
    Name of sort algorithm:             bubble_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.045157 sec
    Min time of sort:                   0.042051 sec
    Max time of sort:                   0.051551 sec
    Pure CPU time per core:             1.3547 sec
    Number of workers (cores):          3 
    In comparison with built-in Tim Sort: 518.39x slower
    =========================================================================
    ```
---
# 🛠️ How to test your own implementation?

Your custom sorting algorithm only needs to accept an unsorted list as an argument. Like this:

```def bubble_sort(arr: list): ```

The specific return format of the function doesn't matter, as long as the algorithm properly sorts the input array in place.

To run a test, simply import your function and add it to the list_of_methods in test_pure_python.py (if it works with standard Python lists) or in test_numpy.py (if it works with NumPy arrays) 🎯.

---

## 📦 Installation

Before running the tests, you need to install the required external libraries (`numpy`, `numba`). You can easily do this using `pip`:

```bash
git clone [https://github.com/angelet-dev/sort-algorithms.git](https://github.com/angelet-dev/sort-algorithms.git)
cd sort-algorithms
pip install -r requirements.txt
```

---

# 🚨 Error Handling

If a sorting algorithm fails to sort the array properly, the framework will detect it and raise the following error:

```python
[ERROR] CRITICAL: <algorithm_name> FAILED TO SORT THE ARRAY!
AssertionError: Algorithm <algorithm_name> is broken!
```


## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.