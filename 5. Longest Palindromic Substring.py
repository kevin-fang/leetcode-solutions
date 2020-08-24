class Solution(object):
    def __init__(self):
        self.existing = set()
        self.max_frames = 10000
    
    def longestPalindromeHelper(self, s, start, end):
        if (start, end) in self.existing:
            return (start, end)
        if abs(start - end) == 1 and s[start] == s[end]:
            return start, end
        """
        :type s: str
        :rtype: str
        """
        if end - start == 0:
            return start, end
        elif s[start] == s[end] and ((start + 1, end - 1) in self.existing or self.longestPalindromeHelper(s, start + 1, end - 1) == (start + 1, end - 1)):
            self.existing.add((start, end))
            #print("palindrome: ", s[start], s[end], s[start:end])
            return (start, end)
        else:
            first_start, first_end = self.longestPalindromeHelper(s, start, end - 1)
            second_start, second_end = self.longestPalindromeHelper(s, start + 1, end)
            largest = max((first_start, first_end), (second_start, second_end), key=lambda x: x[1] - x[0])
            self.existing.add((first_start, first_end))
            self.existing.add((second_start, second_end))
            return largest
    
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        start, end = self.longestPalindromeHelper(s, 0, len(s) - 1)
        return s[start:end + 1]
