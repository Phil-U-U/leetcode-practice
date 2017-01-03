'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.

Author: Phil H. Cui
Date: 01/02/16

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        lookup = {}

        for string in strs:
        	sorted_string = ''.join(sorted(string))
        
        	if sorted_string not in lookup:# not lookup.get( sorted_string, False ):
        		lookup[sorted_string] = [string]
        	else:
        		lookup[sorted_string].append(string)

        return [val for key, val in lookup.iteritems()]
        	


if __name__ == "__main__":

	print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])