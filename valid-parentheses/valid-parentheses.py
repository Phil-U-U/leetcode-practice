'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Author: Phil H. Cui
Date:   12/08/16

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass

if __name__ == "__main__":
    s = "()[]{}"
    print Solution().isValid( s )

    s1 = "([)]"
    print Solution().isValid( s1 )
