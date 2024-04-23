class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s:
            if char in mapping:
                stack.append(char)
            elif stack and mapping[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack


print(Solution().isValid("([])"))
