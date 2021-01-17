class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        uselist = []
        result = []
        
        digdict = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j","k","l"], "6": ["m","n","o"], "7": ["p","q","r","s"], "8": ["t","u","v"], "9": ["w","x","y","z"]}
        
        if len(digits) == 1:
            return "".join(digdict[digits])
        
        for d in digits:
            uselist.append(digdict[d])
                
        if len(uselist) == 2:
            for i in uselist[0]:
                for j in uselist[1]:
                    result.append(i+j)
        elif len(uselist) == 3:
            for i in uselist[0]:
                for j in uselist[1]:
                    for k in uselist[2]:
                        result.append(i+j+k)
        elif len(uselist) == 4:
            for i in uselist[0]:
                for j in uselist[1]:
                    for k in uselist[2]:
                        for l in uselist[3]:
                            result.append(i+j+k+l)
        return result
