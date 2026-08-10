from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 3:53 PM ~
        # M1: Brute force
        # for each s element, compare t element and if found in t, remove that element. If every element in s found in t, return True (valid), otherwise return False
        # Time: O(n^2), Space: O(1) just compare directly. But can be really confusing by removing the t ... and actually we can't remove t cuz its string......... then need to convert str to list first.
        # M2: use counters to calculate s and t's characters.
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count

        