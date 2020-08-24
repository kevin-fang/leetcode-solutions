class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        if len(s) == 1 and s not in wordDict:
            return False

        table = [None] * len(s)
        if table[0] in wordDict:
            table[0] = 1

        for idx in range(len(s)):
            if s[0:idx + 1] in wordDict:
                table[idx] = 1
                continue
            if table[idx] is not None:
                continue
            for word in wordDict:
                length = len(word)
                chunk = s[idx - length + 1:idx + 1]
                if chunk in wordDict and table[idx - length]:
                    table[idx] = 1
                    break
                else:
                    table[idx] = 0

        return True if table[-1] else False
