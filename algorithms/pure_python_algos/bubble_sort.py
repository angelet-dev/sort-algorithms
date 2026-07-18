def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(n):
            num_1 = arr[i]
            num_2 = arr[j]
            if num_1 < num_2 and i != j:
                arr[j] = num_1
                arr[i] = num_2

    return arr
