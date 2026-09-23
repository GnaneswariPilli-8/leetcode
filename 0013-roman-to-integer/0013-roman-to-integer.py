class Solution(object):
    def value(self,r):
            if r == 'I':
                return 1
            elif r == 'V':
                return 5
            elif r == 'X':
                return 10
            elif r == 'L':
                return 50
            elif r == 'C':
                return 100
            elif r == 'D':
                return 500
            elif r == 'M':
                return 1000
    def romanToInt(self, s):
        total = 0

        for i in range(len(s)):
            n1 = self.value(s[i])

            if i + 1 < len(s):
                n2 = self.value(s[i + 1])

                if n1 < n2:
                    total -= n1
                else:
                    total += n1
            else:
                total += n1

        return total
        