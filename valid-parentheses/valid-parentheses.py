'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

解题方法是：

一个个检查给的characters，如果是左括号都入栈；如果是右括号，检查栈如果为空，证明不能匹配，如果栈不空，弹出top，与当前扫描的括号检查是否匹配。

全部字符都检查完了以后，判断栈是否为空，空则正确都匹配，不空则证明有没匹配的。



Author: Phil H. Cui
Date:   12/10/16
'''

class Solution(object):
    def isValid(self, S):
        """
        :type s: str
        :rtype: bool
        """
        # stack, match
        stack = []
        pairs = {'()', '[]', '{}'}

        for s in S:
            if s in '([{':
                stack.append(s)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop()+s not in pairs:
                        return False

        return not stack

    def isValid_2( self, S):

        stack = []
        lookup = {'(':')', '[':']', '{':'}'}

        for s in S:
            if s in lookup:
                stack.append(s)
            else:
                if not stack or lookup[stack.pop()] != s:
                    return False

        return not stack

if __name__ == "__main__":
    s = "()[]{}"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid_2( s )  )

    s1 = "([)]"
    print "Expected:{}-Calculated:{}".format( "False", Solution().isValid_2( s1 ) )

    s2 = "([])"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid_2( s2 ) )

    s3 = "([]{})"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid_2( s3 ) )
