class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 2:56 PM ~
        return len(set(nums)) != len(nums)