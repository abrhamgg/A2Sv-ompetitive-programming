class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new_dict = {}
        rep = []
        nums = sorted(nums)
        for i in nums:
            if i in new_dict.keys():
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        d = (sorted(new_dict.items(), key=lambda item: item[1]))
        t = d[-k:]
        rep = [i[0] for i in t]
        return rep
