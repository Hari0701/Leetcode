class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        m = 0
        while left < right:
            m = max((min(height[left], height[right]) * (right-left)),m)
            if height[left] <= height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -=1
        return m