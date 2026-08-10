class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 2:56 PM ~ 2:59PM
        # Method 1: Brute force
        # Time: O(n^2), Space: O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False

        # Method 2: Hash set
        # Time: O(n), Space: O(n)
        # seen = []
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     seen.append(nums[i])
        # return False

        # Method 3: Compare length
        return len(set(nums)) != len(nums)