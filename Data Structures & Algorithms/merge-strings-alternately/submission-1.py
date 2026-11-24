class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        word3 = ""
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                word3 += word1[p1]
                p1 += 1
            if p2 < len(word2):
                word3 += word2[p2]
                p2 += 1
        return word3
