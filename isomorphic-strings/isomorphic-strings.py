'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Author: Phil H. Cui
Date: 12/01/16
'''

class Solution( object ):
    def findIsomorphicStrings( self, s, t):

        lookup_s, lookup_t = dict(), dict()

        for i in xrange( len(s) ):

            target, source = lookup_s.get( s[i] ), lookup_t.get( t[i] )
            if source is None and target is None:
                lookup_s[ s[i] ], lookup_t[ t[i] ] = t[i], s[i]
            elif target != t[i] or source != s[i]:
                return False

        return True

if __name__ == "__main__":
    s, t = 'egg', 'add'
    print "Expected:{}-{}".format( True, Solution().findIsomorphicStrings( s, t ) )

    s, t = 'foo', 'bar'
    print "Expected:{}-{}".format( False, Solution().findIsomorphicStrings( s, t ) )

    s, t = 'paper', 'title'
    print "Expected:{}-{}".format( True, Solution().findIsomorphicStrings( s, t ) )
