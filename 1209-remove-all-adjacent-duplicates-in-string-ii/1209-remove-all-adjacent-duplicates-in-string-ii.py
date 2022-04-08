class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # i = 0
        # length = len(s)
        # while i <= length -2:
        #     if len(set(s[i:i + k])) == 1 and len(s) > k:
        #         left = s[0:i]
        #         right = s[i+k:]
        #         s = left + right
        #         i = 0
        #     else:  
        #         i += k
        # return s 
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[i], 1])
        
        res = ""
        for ch, cnt in stack:
            res += ch*cnt
        
        return res   