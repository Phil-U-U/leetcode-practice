'''

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Author: Phil H. Cui
Date: 12/26/16

'''
from string import punctuation

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return None

        start = 0
        for i, char in enumerate(str):
            if char != ' ':
                start = i
                break

        if start == len(str)-1:
            return None
        else:
            str = str[start:]


        not_valid = punctuation.replace('+','-').replace('-','')
        if str[0] in not_valid:
            return None

        for i, char in enumerate(str):
            if char[0]

            # ord, result * 10 + x


if __name__ == "__main__":
    string = "82"  # "+82", "-82", "82*&*", "%$&82", "", "   ",
    print Solution().myAtoi()
