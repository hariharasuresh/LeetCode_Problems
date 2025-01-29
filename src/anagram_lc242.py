class AnagramSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars_count = [0] * 26
        for i in range(len(s)):
            chars_count[ord(s[i]) - ord('a')] += 1
            chars_count[ord(t[i]) - ord('a')] -= 1
        for count in chars_count:
            if (count != 0):
                return False
        return True
