class Solution:
    @cache
    def tribonacci(self, nums: int) -> int:
        if nums == 0:
            return 0
        elif nums < 3:
            return 1
        else:
            return self.tribonacci(nums-1) + self.tribonacci(nums-2) + self.tribonacci(nums-3) 