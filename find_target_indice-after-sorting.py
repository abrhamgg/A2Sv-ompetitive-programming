class Solution(object):
    def insertionSort1(self, n, arr):
        for i in range(n):
            j = i - 1
            while(i != 0 and arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j += -1
                i += -1
        return arr

    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = self.insertionSort1(len(nums), nums)
        new = []
        for i in range(len(nums)):
            if nums[i] == target:
                new.append(i)
        return new