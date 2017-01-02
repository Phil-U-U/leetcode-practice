'''
Time: O(n)
Space:O(1)

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
 
The input string does not contain leading or trailing spaces and the words are always separated by a single space.
 
For example,
Given s = "the sky is blue",
return "blue is sky the".
 
Could you do it in-place without allocating extra space?

Author: Phil H. Cui
Date: 01/02/2017
'''

class Solution( object ):
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        


if __name__ == '__main__':
    s = ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
    Solution().reverseWords(s)
    print s