class Solution:
    def check(self,nums,mid,m):
        sumz = 0
        c = 1
        n = len(nums)     
        
        for i in range(n):
            if nums[i] + sumz <= mid:
                sumz += nums[i]
                
            else:
                c += 1 
                if c > m or nums[i] > mid:
                    return False
                    
                sumz = nums[i]
        
        return True        
    
    def splitArray(self, nums: List[int], m: int) -> int:
        start = 0 
        end = sum(nums)
        
        ans = -1
        
        while start <= end:
            mid = start + (end - start)//2
            
			#if true then mid can be possible answer so store in ans
            if self.check(nums,mid,m):
                ans = mid
                end = mid - 1
                
            else:
                start = mid + 1
                
        return ans