class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        freq = {}
        for string in strs:
            chars = [0] * 26
            for c in string:
                chars[alphabet.index(c)] += 1
            if len(freq.get(tuple(chars), [])) != 0:
                freq[tuple(chars)].append(string)
            else:
                freq[tuple(chars)] = [string]
        for v in freq.values():
            res.append(v)
        return res
            


        