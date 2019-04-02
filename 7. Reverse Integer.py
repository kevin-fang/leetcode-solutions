class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed = None
        if x < 0:
            reversed = -int(str(x)[::-1][:-1])
        else:
            reversed = int(str(x)[::-1])
        if reversed < -2 ** 31 or reversed > 2 ** 31 - 1:
            return 0
        return reversed
