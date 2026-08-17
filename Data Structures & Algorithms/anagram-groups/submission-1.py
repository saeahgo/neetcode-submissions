from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 9:59 PM ~ 
        # brute force: check every str if its sorted is the same and put it in hash map... then... Time: O(nlogn) since we are sorting...? ah if we set m is the number of strings, O(m * nlogn) where n is the length of the longest string. Space: O(m)

        # If we don't use sorting...... we can count the number of characters as well! Then use Counter, and if the Counter value is the same, then put them into the same hash map. Then... Time: O(mn), space: O(m)? I think this method is better. Ah, actually instead of using Counter, if we use [0] * 26 count array, we can do O(1) as 26 is a constant number.
        seen = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            seen[key].append(s)
        
        return list(seen.values())
            


        