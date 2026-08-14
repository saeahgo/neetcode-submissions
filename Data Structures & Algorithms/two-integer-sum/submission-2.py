class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: use nested loop to check if two sums are the target. Time: O(n^2), Space: O(1) - only use variables
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # use hash map to store the seen value, and find seen value's indices if two sums are the target. Time: O(n) - one loop only, Space: O(n) - can be increased as n increase (for the hash set)
        seen = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in seen:
                return [seen[temp], i]
            seen[nums[i]] = i