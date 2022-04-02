class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            n = len(nums)
            if n == 1:
                return nums
            
            mid = (0 + n)//2
            
            left_partition = mergesort(nums[:mid])
            right_partition = mergesort(nums[mid:])
            
            return merge(left_partition, right_partition)
        
        def merge(lp, rp):
            i = j = 0
            output = []
            
            while i < len(lp) and j < len(rp):
                if lp[i] < rp[j]:
                    output.append(lp[i])
                    i += 1
                else:
                    output.append(rp[j])
                    j += 1      
            output.extend(lp[i:])
            output.extend(rp[j:])
            return output       
            
        sortedArray = mergesort(nums)
        return sortedArray