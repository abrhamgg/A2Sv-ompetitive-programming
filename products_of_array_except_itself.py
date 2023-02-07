class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = [0]* len(nums)
        product[0] = 1
        for i in range(1, len(nums)):
            product[i] = nums[i-1] * product[i - 1]
        
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] = product[i] * suffix_product
            suffix_product = suffix_product * nums[i]
        return product
