class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        minimum = 0
        maxvol = 0
        currlist = []
        vol = 0
        if len(height) == 2:
            minimum = min(height)
            return minimum
        while len(height) != 0:
            minimum = min(height[0], height[-1])
            maxvol = max(maxvol, minimum * (len(height)-1))
            if height[0] < height[-1]:
                height = height[1:]
            else:
                height = height[:-1]
        return maxvol
