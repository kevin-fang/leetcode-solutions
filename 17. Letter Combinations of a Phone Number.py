class Solution(object):
    def getMappings(self):
        return {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    def letterCombinationsHelper(self, digits, char_idx):
        if char_idx <= 0:
            return list(self.getMappings()[digits[0]])
        else: 
            digit = digits[char_idx]
            smaller_lst = self.letterCombinationsHelper(digits, char_idx - 1)
            new_result = []
            for i in smaller_lst:
                for letter in self.getMappings()[digit]:
                    new_result.append(i + letter)
            return new_result
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        return self.letterCombinationsHelper(digits, len(digits) - 1)
