class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        substring = []
        
        for i in s:
            if i in substring:
                substring = substring[substring.index(i)+1:]
            substring.append(i)
            maximum = max(maximum, len(substring))
        return maximum
                
            
