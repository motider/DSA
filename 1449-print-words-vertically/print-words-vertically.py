class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        for word in words:
            x = len(word)
            if x > max_len:
                max_len = x
            for i in range(len(words)):
                while len(words[i]) < max_len:
                    words[i] += " "
            lists = []
            for letters in zip(*words):
                lists.append("".join(letters).rstrip())

        return lists

