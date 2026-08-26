class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = s.lower()
        alpha_s = ''.join(char for char in low_s if char.isalnum())
        result = alpha_s.replace(" ", "")
        i = 0
        j = len(result)-1
        print(i, j)
        while i < j:
            if result[i] != result[j]:
                print(result[i], result[j])
                return False
            i += 1
            j -= 1
        
        return True

        