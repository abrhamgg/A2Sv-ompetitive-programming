class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        n = len(s)
        if n == 0 or n == 1:
            return True
        if n % 2 == 0:
            j = n - 1
            print(s)
            for i in range(n//2 + 1):
                print(i,j)
                print(s[i], s[j])
                if s[i] != s[j]:
                    return False
                j -= 1
            return True
        else:
            j = n - 1
            for i in range(n//2 + 1):
                if s[i] != s[j]:
                    return False
                j = j - 1
            return True
