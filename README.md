# 🚀 sort-algorithms

**sort-algorithms is a future library containing my implementations of various sorting algorithms.**

---
## 📦 What does it contain right now?

* **merge sort**: ⚡️ my implementation of the classic merge sort algorithm.
* **bad merge sort**: 🐢 my implementation of the main idea of merge sort without creating additional arrays (which led to performance degradation).
* **bubble sort**: 🐌 included just for performance comparison with the bad merge sort.
* **test.py**: 🧪 a testing framework to evaluate these algorithms. I built everything needed to run benchmarks and gather statistics.

---
## 📊 Output Examples (test.py)

* **Example 1: Testing merge sort on a massive dataset** 🏎️

    Parameters:
    ```python
    N = 10000000
    iteration = 3
    list_of_methods = [merge_sort]
    ```
    Output:

    ```bash
    =========================================================================
                                    RESULTS                  
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        10,000,000
    Number of iterations:               3
    Mean time of sort:                  67.335583 sec
    Min time of sort:                   66.564636 sec
    Max time of sort:                   67.732268 sec
    In comparison with built-in:        15.56x slower
    =========================================================================
    ```

* **Example 2: Testing and comparing all sorts** 🥊

    Parameters:
    ```python
    N = 10000
    iteration = 30 
    list_of_methods = [merge_sort, bed_merge_sort, bubble_sort]
    ```

    Output:
    ```bash
    =========================================================================
                                    RESULTS                  
    =========================================================================
    Name of sort algorithm:             merge_sort
    Number of elements in array:        10,000
    Number of iterations:               30
    Mean time of sort:                  0.035577 sec
    Min time of sort:                   0.028933 sec
    Max time of sort:                   0.052431 sec
    In comparison with built-in:        23.84x slower
    =========================================================================
    Name of sort algorithm:             bad_merge_sort
    Number of elements in array:        10,000
    Number of iterations:               30
    Mean time of sort:                  7.419627 sec
    Min time of sort:                   5.578328 sec
    Max time of sort:                   9.098767 sec
    In comparison with built-in:        4971.17x slower
    =========================================================================
    Name of sort algorithm:             bubble_sort
    Number of elements in array:        10,000
    Number of iterations:               30
    Mean time of sort:                  15.243006 sec
    Min time of sort:                   9.351046 sec
    Max time of sort:                   17.217606 sec
    In comparison with built-in:        10212.85x slower
    =========================================================================
    ```

---
# 🛠️ How to test your own implementation?

Your custom sorting algorithm only needs to accept an unsorted list as an argument. Like this:

```def bubble_sort(arr: list): ```

The specific return format of the function doesn't matter, as long as the algorithm properly sorts the input array in place.

To run a test, just import your function and add it to the list_of_methods in test.py 🎯.

---

## 📦 Installation

Before running the tests, you need to install the required external libraries (`numpy`). You can easily do this using `pip`:

```bash
pip install -r requirements.txt
```

---

# 🚨 Error Handling

If a sorting algorithm fails to sort the array properly, the framework will detect it and raise the following error:

```python
[ERROR] CRITICAL: bubble_sort FAILED TO SORT THE ARRAY!
AssertionError: Algorithm bubble_sort is broken!
```


## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.