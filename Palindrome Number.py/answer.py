class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_string = str(x)
        backwards_number = x_string[::-1]

        if backwards_number == x_string:
            return True
        else:
            return False


# Test
solution = Solution()
solution.isPalindrome(121)
