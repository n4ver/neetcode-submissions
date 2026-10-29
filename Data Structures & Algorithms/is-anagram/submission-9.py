class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for s_char, t_char in zip(s, t):
            freq[s_char] = freq.get(s_char, 0) + 1
            freq[t_char] = freq.get(t_char, 0) - 1

        return all(count == 0 for count in freq.values())