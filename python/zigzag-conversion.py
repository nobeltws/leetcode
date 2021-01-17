class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rstr = ""
        dir = 0
        list1 = []
        
        if numRows == 1:
            return s
        if numRows == 2:
            string1 = s[0::2]
            string2 = s[1::2]
            return string1+string2
        for i in range(numRows):
            list1.append([])
        while len(s) != 0:
            if dir == 0:
                for j in range(numRows-1):
                    if len(s) != 0:
                        list1[j].append(s[0])
                        s = s[1:]
                    else:
                        break
                dir = 1
            else:
                for k in range(numRows-1,0,-1):
                    if len(s) != 0:
                        list1[k].append(s[0])
                        s =s[1:]
                    else:
                        break
                dir = 0
        for arr in list1:
            rstr += "".join(arr)
        return rstr
                    
