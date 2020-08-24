import collections
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
		    return False
        d = collections.deque()

        for char in s:

            if char in [")", "}", "]"]:
                if (len(d) == 0):
                    return False
                
                last_char = d.popleft()

            if char == ")":
                if last_char == "(":
                    continue
                else:
                    d.appendleft(char)
            elif char == "}":
                if last_char == "{":
                    continue
                else:
                    d.appendleft(char)
            elif char == "]":
                if last_char == "[":
                    continue
                else:
                    d.appendleft(char)
            else:
                d.appendleft(char)

        if len(d) != 0:
            return False
        return True
