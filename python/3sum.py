from itertools import combinations
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                need = -nums[i] - nums[j]
                find_need = bisect.bisect_left(nums, need, j+1, len(nums)-1)
                if nums[find_need] == need:
                    result.add((nums[i], nums[j],nums[find_need]))
        return result
    
