class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        res = {}
        for i,num in enumerate(nums):
            res[num] = i
        for x, y in operations:
            k = res[x]
            nums[k] = y
            res[y] = k
            del res[x]
        return nums
