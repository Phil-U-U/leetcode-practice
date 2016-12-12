'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].


Author: Phil H. Cui
Date: 10/12/16

'''


class Solution(object):
    def findRepeatedDnaSequences(self, S):
        """
        :type s: str
        :rtype: List[str]
        """

        lookup = {}
        res = []

        for i, _ in enumerate(S):
            cur = S[i:i+10]
            # print cur
            if cur not in lookup:
                lookup[cur] = 1
            else:
                lookup[cur] += 1
                if lookup[cur] == 2:
                    res.append(cur)

        return res#, lookup

if __name__ == "__main__":
    S = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print Solution().findRepeatedDnaSequences( S )

    S2 = "AAAAAAAAAAAA"
    print Solution().findRepeatedDnaSequences( S2 )

    #
    # ["AAAAA AAAAA",
    #  "AAAAA AAAAA"]
