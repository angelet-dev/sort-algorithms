import math


def merge_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    temp_arr = arr.copy()
    steps = math.ceil(math.log2(n))
    for step in range(steps + 1):
        size = 2 ** (step + 1)
        temp_arr = arr.copy()
        for i in range(math.ceil(n / size)):
            start_idx = i * size
            mid_idx = start_idx + size // 2
            end_inx = min((i + 1) * size - 1, n - 1)
            left_idx = start_idx
            right_idx = mid_idx
            if right_idx > n - 1:
                break
            left_val = temp_arr[left_idx]
            right_val = temp_arr[right_idx]

            for j in range(end_inx - start_idx + 1):
                if left_val is not None and right_val is not None:
                    if left_val > right_val:
                        arr[start_idx + j] = right_val
                        right_idx += 1
                        right_val = (
                            temp_arr[right_idx] if right_idx <= end_inx else None
                        )
                    else:
                        arr[start_idx + j] = left_val
                        left_idx += 1
                        left_val = temp_arr[left_idx] if left_idx < mid_idx else None
                else:
                    if left_val is not None:
                        arr[start_idx + j : end_inx + 1] = temp_arr[left_idx:mid_idx]
                        break
                    elif right_val is not None:
                        arr[start_idx + j : end_inx + 1] = temp_arr[
                            right_idx : end_inx + 1
                        ]
                        break

    return arr
