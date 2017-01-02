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
    # def reverseWords(self, s):
    	
    # 	words = s.split()

    # 	n = len(words)

    # 	for i in xrange(n/2):
    		
    # 		words[i], words[n-1-i] = words[n-1-i], words[i]

    # 	return ' '.join(words)	

    def reverseWords( self, s):

    	self.reverse( s ) 					#, 0, len(s))
    	i = 0

    	for j, char in enumerate(s):

    		if char == " " or j == len(s)-1:
    			self.reverse( s[i:j] )
    			i = j + 1




    def reverse( self, s): #, start, end):

    	n = len(s) # end - start
    	for i in xrange(n/2):
    		s[i], s[n-1-i] = s[n-1-i], s[i]





if __name__ == '__main__':
	# s = "skyIs"
    
    s = ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
    # s = "the sky is blue"
    Solution().reverseWords(s)
    print ' '.join(s)
    