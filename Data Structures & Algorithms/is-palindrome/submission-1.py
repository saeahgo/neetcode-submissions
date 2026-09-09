class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "") # remove whitespace
        s = s.lower() # make all characters lower
        s = "".join(char for char in s if char.isalnum())
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        