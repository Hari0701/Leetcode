# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         for i in nums:
#             freq[i] = freq[i]+ 1 if i in freq else 1        
#         freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
#         return([*freq][0:k])
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        if k == len(nums):
            return nums
        count = Counter(nums)   

        return heapq.nlargest(k, count.keys(), key=count.get)     
    
    