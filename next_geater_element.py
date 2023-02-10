class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_list = []
        l = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    s=0
                    for k in nums2[j+1:]:
                        if k > i:
                            s=k
                            break
                    if not s:
                        l.append(-1)
                    else:l.append(k)       
        return l[:len(nums1)]              
