class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for letter in s:
        if letter in pairs:
