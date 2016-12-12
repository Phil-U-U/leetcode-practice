'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

双指针，动态维护一个区间。尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符后，然后再收缩头指针，直到不能再收缩为止。最后记录所有可能的情况中窗口最小的.
http://www.cnblogs.com/TenosDoIt/p/3461301.html

Author: Phil H. Cui
Date: 12/08/16


'''
class Solution(object):
    def minWindow(self, S, T):
        """ :type s: str  :type t: str :rtype: str """
        cur_count, expected_count = {}, {}  #count lookup， expected_count： "set the standard"

        i, start = 0, 0  # i: scan pointer, # start marks the start of the window
        min_start, min_width = 0, float("inf")  # return result s[min_start:min_start+min_width]
        cnt = 0 # number of character in t that has been included in the window
        for char in T:
            if char not in expected_count:
                expected_count[char] = 1
                cur_count[char] = 0
            else:
                expected_count[char] += 1

        while i < len(S):
            # Move the second window bar to where all letters in T are included,
            if S[i] in T:
                cur_count[ S[i] ] += 1

            # After the window includes T, no longer functions.
            if S[i] in T and cur_count[ S[i] ] <= expected_count[ S[i] ]:
                cnt += 1

            # Shrink the first window bar to a minimum window that include all letters in T
            if cnt == len(T):
                while S[start] not in T or cur_count[ S[start] ] > expected_count[ S[start] ]  :
                # cur_count[ S[start] ]的值会被cur_count[ S[i] ]的更新而修改，从而触发循环开始而shrink window到最优
                    if S[start] in T:
                        cur_count[ S[start] ] -= 1
                    start += 1

                if i - start + 1 < min_width:
                    min_start = start
                    min_width = i - start + 1
                    print S[min_start:min_start+min_width]

            print S[i], cur_count, expected_count
            i += 1

        if min_width == float("inf"):
            return ""
        else:
            return S[min_start:min_start+min_width]



if __name__ == "__main__":
    # S, T = "ADOBECODEBANC", "ABC"
    S, T = "ebadbaccb", "abc"
    print Solution().minWindow( S, T )
