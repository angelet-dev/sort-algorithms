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
* **Save reports**: Simply change `save_report` from `False` to `True` to automatically save benchmark reports into the `reports/` directory as a `.txt` file for future analysis.
* **Logs**: Monitor the entire benchmarking process via real-time console logs, or easily turn them off if you prefer a clean terminal.
---

## 📊 Output Examples (test.py)

* **Example 1: Running `test_numpy.py`** 🏎️

    Parameters:
    ```python
    # List of all algorithms to test
    list_of_methods = [numba_merge_sort]

    N = 10000000  # Size of the unsorted array
    iterations = 18  #  Number of unique unsorted arrays to test
    num_workers = 4  # Number of parallel processes
    built_in_sort: Literal["quicksort", "mergesort", "heapsort", "stable"] = "quicksort"  # NumPy built-in sort algorithm for comparison
    save_report = False  # True - save report of benchmark to .txt | False - pass
    DTYPE: Literal["int64", "float64"] = "float64"  # Data type of elements in array

    ```
    Output:

    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    DTYPE = float64  
    Mean time of build-in NumPy quicksort = 0.136329 sec                       
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        10,000,000
    Number of iterations:               18
    Mean time of sort:                  1.781694 sec
    Min time of sort:                   1.681049 sec
    Max time of sort:                   1.921536 sec
    Pure CPU time per core:             8.0176 sec
    Number of workers (cores):          4 
    In comparison with build-in NumPy quicksort: 13.07x slower
    =========================================================================
    ```

* **Example 2: Testing and comparing multiple algorithms in `test_numpy.py`** 

    Parameters:
    ```python
    list_of_methods = [numba_merge_sort, merge_sort, bad_merge_sort, bubble_sort]

    N = 5000  
    iterations = 50  
    num_workers = 4  
    built_in_sort: Literal["quicksort", "mergesort", "heapsort", "stable"] = "quicksort"  
    save_report = False  
    DTYPE: Literal["int64", "float64"] = "float64" 
    ```

    Output:
    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    DTYPE = float64  
    Mean time of build-in NumPy quicksort = 0.000044 sec                       
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        5,000
    Number of iterations:               50
    Mean time of sort:                  0.000615 sec
    Min time of sort:                   0.000502 sec
    Max time of sort:                   0.000945 sec
    Pure CPU time per core:             0.0077 sec
    Number of workers (cores):          4 
    In comparison with build-in NumPy quicksort: 13.95x slower
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        5,000
    Number of iterations:               50
    Mean time of sort:                  0.025938 sec
    Min time of sort:                   0.015422 sec
    Max time of sort:                   0.054569 sec
    Pure CPU time per core:             0.3242 sec
    Number of workers (cores):          4 
    In comparison with build-in NumPy quicksort: 588.14x slower
    =========================================================================
    Name of sort algorithm:             bad_merge_sort
    Number of elements in array:        5,000
    Number of iterations:               50
    Mean time of sort:                  2.485507 sec
    Min time of sort:                   1.896400 sec
    Max time of sort:                   2.959303 sec
    Pure CPU time per core:             31.0688 sec
    Number of workers (cores):          4 
    In comparison with build-in NumPy quicksort: 56359.02x slower
    =========================================================================
    Name of sort algorithm:             bubble_sort
    Number of elements in array:        5,000
    Number of iterations:               50
    Mean time of sort:                  8.032859 sec
    Min time of sort:                   6.175907 sec
    Max time of sort:                   10.140253 sec
    Pure CPU time per core:             100.4107 sec
    Number of workers (cores):          4 
    In comparison with build-in NumPy quicksort: 182145.54x slower
    =========================================================================
    ```

* **Example 3: Running `test_pure_python.py`** 

    Parameters:
    ```python
    # List of all algorithms to test
    list_of_methods = [numba_merge_sort]

    N = 10000000  # Size of the unsorted array
    iterations = 18  # Number of unique unsorted arrays to test
    num_workers = 4  # Number of parallel processes
    save_report = False  # True - save report of benchmark to .txt | False - pass
    DTYPE: Literal["int", "float"] = "float"  # Data type of elements in array
    ```

    Output:
    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    DTYPE = float  
    Mean time of built-in Tim Sort = 3.921467 sec                       
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        10,000,000
    Number of iterations:               18
    Mean time of sort:                  15.041842 sec
    Min time of sort:                   12.074183 sec
    Max time of sort:                   16.882942 sec
    Pure CPU time per core:             67.6883 sec
    Number of workers (cores):          4 
    In comparison with built-in Tim Sort: 3.84x slower
    =========================================================================
    ```

* **Example 4:  Testing and comparing all sorts in `test_pure_python.py`** 

    Parameters:
    ```python
    list_of_methods = [numba_merge_sort, merge_sort, bad_merge_sort, bubble_sort]

    N = 1000  
    iterations = 90  
    num_workers = 4 
    save_report = False  
    DTYPE: Literal["int", "float"] = "float"  

    ```

    Output:
    ```bash
    =========================================================================
                                RESULTS                  
    =========================================================================
    DTYPE = float  
    Mean time of built-in Tim Sort = 0.000098 sec                       
    =========================================================================
    Name of sort algorithm:             numba_merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.001315 sec
    Min time of sort:                   0.000917 sec
    Max time of sort:                   0.002368 sec
    Pure CPU time per core:             0.0296 sec
    Number of workers (cores):          4 
    In comparison with built-in Tim Sort: 13.40x slower
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.001662 sec
    Min time of sort:                   0.001197 sec
    Max time of sort:                   0.002939 sec
    Pure CPU time per core:             0.0374 sec
    Number of workers (cores):          4 
    In comparison with built-in Tim Sort: 16.93x slower
    =========================================================================
    Name of sort algorithm:             bad_merge_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.029161 sec
    Min time of sort:                   0.024211 sec
    Max time of sort:                   0.055372 sec
    Pure CPU time per core:             0.6561 sec
    Number of workers (cores):          4 
    In comparison with built-in Tim Sort: 297.13x slower
    =========================================================================
    Name of sort algorithm:             bubble_sort
    Number of elements in array:        1,000
    Number of iterations:               90
    Mean time of sort:                  0.043724 sec
    Min time of sort:                   0.039067 sec
    Max time of sort:                   0.084649 sec
    Pure CPU time per core:             0.9838 sec
    Number of workers (cores):          4 
    In comparison with built-in Tim Sort: 445.52x slower
    =========================================================================
    ```
---
# 🛠️ How to test your own implementation?

Your custom sorting algorithm only needs to accept an unsorted list as an argument. Like this:

```def <algorithm_name>(arr: list): ```
or
```def <algorithm_name>(arr: np.array): ```

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