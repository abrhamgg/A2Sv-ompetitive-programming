class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        new = []
        for i in nums:
            new.append(int(i))
        new = sorted(new)
        value = new[len(nums) - k]
        for i in range(len(nums)):
            if value == int(nums[i]):
                return nums[i]
