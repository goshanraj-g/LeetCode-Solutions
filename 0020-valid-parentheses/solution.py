class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return len(stack) == 0
