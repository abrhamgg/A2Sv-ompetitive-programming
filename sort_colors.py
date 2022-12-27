class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp =[0,0,0]
        for i in range(len(nums)):
            if nums[i] == 0:
                temp[0] += 1
            elif nums[i] == 1:
                temp[1] += 1
            elif nums[i] == 2:
                temp[2] += 1
        for i in range(len(temp)):
            for a in range(temp[0]):
                nums[a] = 0
            for j in range(temp[0], temp[0] + temp[1]):
                nums[j] = 1
            for k in range(temp[0] + temp[1], temp[0]+temp[1]+temp[2]):
                nums[k] = 2
        return nums
