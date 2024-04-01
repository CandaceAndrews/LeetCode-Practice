class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            