class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = sorted(set(nums))
        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = (low-high)// 2 + high
            if(nums[mid] > target):
                high = mid -1
            elif(nums[mid] < target):
                low = mid + 1
            else: 
                return True
        return False    