class Solution: 
    def select(self, arr, i):
        idx = i
        min_value = arr[i]
        for i in range(i, len(arr)):
            if min_value > arr[i]:
                min_value = arr[i]
                idx = i
        return [min_value, idx]

    def selectionSort(self, arr,n):
        for i in range(n):
            data = self.select(arr, i)
            temp = arr[i]
            arr[i] = arr[data[1]]
            arr[data[1]] = temp
