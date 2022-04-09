class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq[i]+ 1 if i in freq else 1        
        freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))
        return([*freq][0:k])      