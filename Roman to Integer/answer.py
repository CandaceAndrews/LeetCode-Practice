class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s) - 1, -1, -1):
            value = roman_values[s[i]]


# solution = Solution()
# solution.romanToInt('XX')
