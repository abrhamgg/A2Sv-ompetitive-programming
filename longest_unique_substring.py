class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        length = int(not not s)
        for char in s:
            if char not in chars:
                chars.append(char)
                length = max(length, len(chars))
            else:
                chars = chars[chars.index(char) + 1:] + [char]
        return length
