class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)

        for i in range(numsLen+1):
            if i not in nums:
                return i
