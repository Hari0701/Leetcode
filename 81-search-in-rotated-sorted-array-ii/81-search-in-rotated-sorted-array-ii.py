class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        nums = sorted(nums)
        low = 0
        high = len(nums)- 1
        while(high >= low):
            mid = (low - high)//2 + high
            if(nums[mid] > target):
                high = mid -1
            elif(nums[mid] < target):
                low = mid + 1
            else:
                return True
        return  False 