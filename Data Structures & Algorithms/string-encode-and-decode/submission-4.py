class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            length = ""
            int_length = 0
            while i < len(s):
                length += s[i]
                i += 1
                if s[i] == "#":
                    int_length = int(length)
                    break
            decoded_strs.append(s[i+1:i+int_length+1])
            i += int_length + 1

        return decoded_strs
