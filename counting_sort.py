def num_occurrence(n, arr):
    count = 0
    for i in arr:
        if n == i:
            count += 1
    return count


def counting_sort(arr):
    freq_arr = [0 for x in range(100)]
    for i in range(100):
        if i in arr:
            freq_arr[i] = num_occurrence(i, arr)
    return freq_arr
