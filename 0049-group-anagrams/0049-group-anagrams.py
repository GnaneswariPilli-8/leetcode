class Solution(object):
    def groupAnagrams(self, strs):
        freq = {}
        for word in strs:
            key = "".join(sorted(word))
            print(key)
            if key not in freq:
                freq[key] = []
            freq[key].append(word)
        return list(freq.values())