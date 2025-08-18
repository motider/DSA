class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        z = ""
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                 z += chars[0]
            else:
                 break

        return z
        