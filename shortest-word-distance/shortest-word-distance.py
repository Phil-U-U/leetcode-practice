'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3. Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Author: Phil H. Cui
Date: 11/25/16

'''


class Solution( object ):
    def __init__( self, words ):
        self.words = words

    def calcShortestDist( self, word1, word2 ):
        dist = float("inf")

        i, idx1, idx2 = 0, None, None
        isNew = False

        while i < len(words):
            if self.words[i] == word1:
                idx1 = i
                isNew = True
            elif self.words[i] == word2:
                idx2 = i
                isNew = True

            if isNew == True and idx1 is not None and idx2 is not None:
                    dist = min( dist, abs(idx1 - idx2) )  # DP
                    isNew = False

            i += 1

        return dist


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1, word2 = "coding", "practice"
    word3, word4 = "makes", "coding"
    shortestDist = Solution( words )
    print 3 - shortestDist.calcShortestDist( word1, word2 )
    print 1 - shortestDist.calcShortestDist( word3, word4 )
