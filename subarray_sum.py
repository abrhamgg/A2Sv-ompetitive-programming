class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        hash = defaultdict(lambda: 0)
        count = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            if sum == k:
                count += 1
            if (sum - k) in hash:
                count += hash[sum - k]
            hash[sum] += 1
        return count
