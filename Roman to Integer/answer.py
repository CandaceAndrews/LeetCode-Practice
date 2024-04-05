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

            if i < len(s) - 1 and roman_values[s[i + 1]] > value:
                result -= value
            else:
                result += value

        return result


# Test
solution = Solution()
solution.romanToInt('XXX')
