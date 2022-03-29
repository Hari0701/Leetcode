class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq[i] + 1 if i in freq  else 1
        for idx, value in freq.items():       
            if value >= 2:
                return idx