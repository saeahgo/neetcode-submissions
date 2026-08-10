from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 3:53 PM ~
        # M1: Brute force
        # for each s element, compare t element and if found in t, remove that element. If every element in s found in t, return True (valid), otherwise return False
        # Time: O(n^2), Space: O(1) just compare directly. But can be really confusing by removing the t ... and actually we can't remove t cuz its string......... then need to convert str to list first.
        # M2: use counters to calculate s and t's characters.
        # Time: O(n), Space: O(1) Since it's just counter (no sorting), time complexity is O(n). space complexity is O(1) since Counter will only have 26 characters, since 26 is a constant, O(1)
        # s_count = Counter(s)
        # t_count = Counter(t)
        # return s_count == t_count

        # Method 3: Sorting
        # Time: O(nlogn), Space:O(n) - sorted() creates new lists, making O(n) space
        # return sorted(s) == sorted(t)

        # Method 4: Fixed Size Array
        # Instead of using Python's Counter, initialize an array of size 26 filled with zeros. count = [0] * 26 And increment counts for characters in s and decrement them for characters in t. If all values end up at 0, it's an anagram. 
        # Time: O(n), Space: O(1)
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for c in count:
            if c != 0:
                return False
        
        return True

        