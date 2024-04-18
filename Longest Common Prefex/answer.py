class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, char in enumerate(str[0]):
            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return strs[0][:i]

        return strs[0]
