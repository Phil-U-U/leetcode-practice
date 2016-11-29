'''
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3. Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Author: Phil H. Cui
Date: 11/26/16

'''

class Solution( object ):
    def __init__( self, words ):
        # self.words = words
        self.lookup = {}
        for i, word in enumerate(words):
            if word not in self.lookup:
                self.lookup[word] = [i]
            else:
                self.lookup[word].append(i)


    def calcShortestDist( self, word1, word2 ):
        res = float("inf")
        idx1 = self.lookup[word1]
        idx2 = self.lookup[word2]

        for i in idx1:
            for j in idx2:
                res = min( res, abs(i-j) )

        return res

    def calcShortestDist_improved( self, word1, word2 ):
        res = float("inf")
        idxes1 = self.lookup[word1]
        idxes2 = self.lookup[word2]

        i, j = 0, 0
        while i < len(idxes1) and j < len(idxes2):
            res = min( res, abs(idxes1[i]-idxes2[j]) )

            if idxes1[i] < idxes2[j]:
                i += 1
            else:
                j += 1


        return res

    def test( self, idxes1, idxes2 ):
        '''
            Merge sorted array, O(M+N)
            Equivalent to find the minimum difference between two sorted array
        since the minimum difference should be between two neighboring numbers
        in a merged and sorted array. (two pointerd)
        '''
        res = float('inf')
        i, j = 0, 0
        while i < len(idxes1) and j < len(idxes2):
            res = min( res, abs(idxes1[i]-idxes2[j]) )

            if idxes1[i] < idxes2[j]:
                i += 1
            else:
                j += 1

        # if i < len(idxes1):
        #     while i < len(idxes1)-1:
        #         res = min( res, abs(idxes1[i]-idxes1[i+1]) )
        #         i += 1
        # else:
        #     while j < len(idxes2)-1:
        #         res = min( res, abs(idxes2[j]-idxes2[j+1]) )
        #         j += 1

        return res

if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1, word2 = "coding", "practice"
    word3, word4 = "makes", "coding"
    solution = Solution(words)
    # print 0 - solution.calcShortestDist( word1, word2 )
    # print 1 - solution.calcShortestDist( word3, word4 )
    print "{}-{}".format(3, solution.calcShortestDist_improved( word1, word2 ) )
    print "{}-{}".format(1, solution.calcShortestDist_improved( word3, word4 ) )

    array1 = [3, 27, 45, 68, 71, 81, 99]
    array2 = [9, 16, 25, 35, 99]
    print "{}-{}".format(0, solution.test( array1, array2))
