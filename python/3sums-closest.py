class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        currsum = sum(nums[0:3])
        result = currsum
        diff = abs(target - currsum)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(i+2, len(nums)):
                    currsum = nums[i] + nums[j] + nums[k]
                    if currsum - target == 0:
                        return currsum
                    elif diff > abs(currsum-target):
                        diff = abs(currsum-target)
                        result = currsum
        return result
