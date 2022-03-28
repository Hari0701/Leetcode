class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        return True if target in nums else False