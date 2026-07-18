import math
import numpy as np

def bad_merge_sort(arr: np.array) -> np.array:
    n = len(arr)
    for i in range(0, math.ceil(math.log2(n))):
        size = 2 ** (i + 1)
        for j in range(math.ceil(n/size)):
            m = range(size // 2)
            for z in m:
                a = j * size + z
                if a >= n:
                    break
                num_1 = arr[a]
                for k in m:
                    b = j * size + size // 2 + k
                    if b >= n:
                        break
                    num_2 = arr[b]
                    if num_1 > num_2:
                        arr[b] = num_1
                        arr[a] = num_2
                        a = b
                    else:
                        break

    return arr


