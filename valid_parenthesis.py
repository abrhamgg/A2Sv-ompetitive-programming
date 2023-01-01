class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    print("empty")
                    return False
                else:
                    top = stack[-1]
                    if (i == ')' and top == '(') or (i == ']' and top == '[') or (i == '}' and top == '{'):
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
