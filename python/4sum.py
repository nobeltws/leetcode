class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        result = set()
        need = 0
        findneed = 0
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    need = target - nums[i] - nums[j] - nums[k]
                    findneed = bisect.bisect_left(nums, need, k+1, len(nums)-1)
                    if nums[findneed] == need:
                        result.add(tuple(sorted([nums[i],nums[j],nums[k],nums[findneed]])))
        return result
