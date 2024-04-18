class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for index, element in enumerate(strs):
            print(index, element)


solution = Solution()
solution.longestCommonPrefix(["flower", "flow", "flight"])
