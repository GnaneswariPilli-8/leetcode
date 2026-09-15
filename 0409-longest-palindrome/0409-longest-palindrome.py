class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        c = 0
        odd = False
        for count in freq.values():
            if count % 2 == 0:
                c += count
            else:
                c += count - 1
                odd = True
        if odd:
            c += 1
        return c
            