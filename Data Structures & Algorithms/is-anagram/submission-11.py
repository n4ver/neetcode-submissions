class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        i = 0
        if len(s) != len(t): return False
        n = len(s)
        while i < n:
            s_char = s[i]
            t_char = t[i]
            if s_char not in freq:
                freq[s_char] = 1
            else:
                freq[s_char] += 1
            if t_char not in freq:
                freq[t_char] = -1
            else:
                freq[t_char] -= 1
            i += 1
        for char in freq.values():
            if char != 0: return False
        return True
        '''
        count = [0] * 26

        for a, b in zip(s, t):
            count[ord(a) - ord('a')] += 1
            count[ord(b) - ord('a')] -= 1

        return all(value == 0 for value in count)
        '''
        