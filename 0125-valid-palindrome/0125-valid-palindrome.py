class Solution(object):
    def isPalindrome(self, s):
        t = ''
        for i in s:
            if i.isalnum():
                t += i
        t = t.lower()
        i = 0
        j = len(t)-1
        while i < j:
            if t[i] != t[j]:
                return False
                break
            i +=1
            j -= 1
        return True