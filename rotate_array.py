class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        offset = len(nums) - k
        for i in range(offset):
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)
        
        return nums
