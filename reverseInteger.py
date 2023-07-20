class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        if x == 0:
            return 0
        if x.bit_length() > 32:
            return 0
        if x > 0:
            num = 0
            count = 0
            while x > 0:
                r = x % 10
                if r != 0 or count != 0:
                    num = (num * 10) + r
                    count += 1
                x = x// 10
            print(num.bit_length())
            if num.bit_length() > 31:
                return 0
            return num * sign


