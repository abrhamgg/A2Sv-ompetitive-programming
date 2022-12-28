class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if (i < j+1 and nums[i] == nums[j+1]):
                    count += 1
        return count
