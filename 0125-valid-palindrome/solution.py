class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

        """
        :type s: str
        :rtype: bool
        """
        
