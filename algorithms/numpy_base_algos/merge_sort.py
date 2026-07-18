import math
from numba import njit
import numpy as np


def merge_sort(arr: np.array) -> None:
    n = len(arr)
    if n <= 1:
        return
    steps = math.ceil(math.log2(n))

    buffer = np.copy(arr)

    read_arr = buffer
    write_arr = arr

    size = 1
    for _ in range(steps):
        size *= 2
        read_arr, write_arr = write_arr, read_arr

        for i in range(math.ceil(n / size)):
            start_idx = i * size
            mid_idx = start_idx + size // 2
            if mid_idx > n - 1:
                write_arr[start_idx:] = read_arr[start_idx:]
                break
            end_idx = min(start_idx + size - 1, n - 1)

            cell_size = end_idx - start_idx + 1

            left_idx = start_idx
            right_idx = mid_idx

            left_val = read_arr[left_idx]
            right_val = read_arr[right_idx]

            for j in range(cell_size):
                if left_val > right_val:
                    write_arr[start_idx + j] = right_val
                    right_idx += 1
                    if right_idx > end_idx:
                        right_val = float("inf")
                        continue
                    right_val = read_arr[right_idx]

                else:
                    write_arr[start_idx + j] = left_val
                    left_idx += 1
                    if left_idx >= mid_idx:
                        left_val = float("inf")
                        continue
                    left_val = read_arr[left_idx]

    if write_arr is not arr:
        arr[:] = write_arr

    return



@njit
def numba_merge_sort(arr: np.array) -> None:
    n = len(arr)
    if n <= 1:
        return
    steps = math.ceil(math.log2(n))

    buffer = np.copy(arr)

    read_arr = buffer
    write_arr = arr

    size = 1
    for _ in range(steps):
        size *= 2
        read_arr, write_arr = write_arr, read_arr

        for i in range(math.ceil(n / size)):
            start_idx = i * size
            mid_idx = start_idx + size // 2
            if mid_idx > n - 1:
                write_arr[start_idx:] = read_arr[start_idx:]
                break
            end_idx = min(start_idx + size - 1, n - 1)

            cell_size = end_idx - start_idx + 1

            left_idx = start_idx
            right_idx = mid_idx

            left_val = read_arr[left_idx]
            right_val = read_arr[right_idx]

            for j in range(cell_size):
                if left_val > right_val:
                    write_arr[start_idx + j] = right_val
                    right_idx += 1
                    if right_idx > end_idx:
                        right_val = float("inf")
                        continue
                    right_val = read_arr[right_idx]

                else:
                    write_arr[start_idx + j] = left_val
                    left_idx += 1
                    if left_idx >= mid_idx:
                        left_val = float("inf")
                        continue
                    left_val = read_arr[left_idx]

    if write_arr is not arr:
        arr[:] = write_arr

    return
