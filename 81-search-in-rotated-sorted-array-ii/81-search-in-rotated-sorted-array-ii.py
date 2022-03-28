class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            while l < m and nums[l] == nums[m]: # two new lines as compared to Q33
                l += 1
            if nums[l] <= target < nums[m]:
                r = m - 1
            elif nums[m] < target <= nums[r]:
                l = m + 1
            elif nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return False