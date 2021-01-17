class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        retstr = ""
        strnum = str(num)
        onesd = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        tensd = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        hundsd = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        thousd = {0: "", 1: "M", 2: "MM", 3: "MMM"}
        while len(strnum) != 0:
            if len(strnum) == 4:
                toconvert = int(strnum) // 1000
                retstr += thousd[toconvert]
                strnum = strnum[1:]
            elif len(strnum) == 3:
                toconvert = int(strnum) // 100
                retstr += hundsd[toconvert]
                strnum = strnum[1:]
            elif len(strnum) == 2:
                toconvert = int(strnum) // 10
                retstr += tensd[toconvert]
                strnum = strnum[1:]
            elif len(strnum) == 1:
                toconvert = int(strnum)
                retstr += onesd[toconvert]
                strnum = ""
        return retstr
