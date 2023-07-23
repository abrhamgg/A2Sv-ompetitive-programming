class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0

        for i, c in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(c)

        return ''.join(result)
