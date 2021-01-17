class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        neg = 0
        num = 0
        rstr = "0"
        whiteflag = 0
        numflag = 0
        strflag = 0
        for i in s:
            if whiteflag == 0 and i == " ":
                continue
            elif whiteflag == 0 and i != " ":
                whiteflag = 1
                if i.isalpha():
                    strflag = 1
                elif i == "-":
                    neg = 1
                    continue
                elif i == "+":
                    continue
      
            if strflag == 0 and whiteflag == 1:
                try:
                    num = int(i)
                    rstr += str(num)
                except:
                    strflag = 1
                    continue
        if neg == 1:
            if abs(int(rstr)) <= pow(2,31):
                return -int(rstr)
            else:
                return -pow(2,31)
        else:
            if int(rstr) <= (pow(2,31)-1):
                return int(rstr)
            else:
                return pow(2,31)-1
