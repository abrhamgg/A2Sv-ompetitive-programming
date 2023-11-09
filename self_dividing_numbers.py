class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        new_list = []

        for num in range(left, right + 1, 1):
            if self.self_divisble(num):
                new_list.append(num)
        return new_list
    def self_divisble(self,num):
        org_num = num
        if num < 10:
            return True
        else:      
            while num > 0:
                last = num % 10
                if last != 0:
                    if org_num % last != 0:
                        return False
                else:
                    return False
                num = num // 10
            return True
    
