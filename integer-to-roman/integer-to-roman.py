'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

字母可以重复，但不超过三次，当需要超过三次时，用与下一位的组合表示：
I: 1, II: 2, III: 3, IV: 4
C: 100, CC: 200, CCC: 300, CD: 400
所以可以将单个罗马字符扩展成组合形式，来避免需要额外处理类似IX这种特殊情况。

Author: Phil H. Cui
Date: 12/12/16

'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 1, 2, 3 - I, II, III
        # 4, 5 - IV, V
        # 6, 7, 8 - VI, VII, VIII
        # 9, 10, 11 - IX, X, XI
        # 50 - L
        # 100 - C
        # 500 - D
        # 1000 - M

        # 998 = 900 + 90 + 8
        #       CM  + XC + VIII


        # 588 = 500 + 80 + 8
        #       D     LXXX  VIII
        #       D     XXC   VIII

        # 3978 = 3000 + 900 + 70 + 8
        #        MMM    CM    LXX  VIII

        res = ""
        romans = ["M", "CM", "D", "CD", "C",  "XC", "L", "XL","X","IX","V","IV","I"]
        val =    [1000, 900, 500, 400,   100,   90,  50,  40,  10, 9,   5,   4,  1]

        for i, roman in enumerate(romans):
            if num >= val[i]:
                res += roman * (num / val[i])
                num %= val[i]

        return res

if __name__ == "__main__":
    print Solution().intToRoman( 3978 )
