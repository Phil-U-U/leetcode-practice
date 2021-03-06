'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Author: Phil H. Cui
Date: 12/31/16
'''


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1

        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1
            if count[c.lower()] < 0:
                return False

        return True


'''
Use Counter
'''
from collections import Counter
class Solution2( object ):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_letters = Counter(s)

        for letter in t:
            if letter not in s_letters:
                return False

            s_letters.subtract(letter)
            if s_letters[letter] == 0:
                s_letters.pop(letter)

        return True

if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    print Solution().isAnagram( s, t )

    s, t = "rat", "car"
    print Solution().isAnagram( s, t )
