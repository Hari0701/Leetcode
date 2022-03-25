class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        index = {}
        stack = []
        for i, v in enumerate(s):
            index[v] = i
        print(index)     
        for i, v in enumerate(s):
            if s[i] in stack:
                continue
            while stack and stack[-1] > v and index[stack[-1]] > i:
                stack.pop()
            stack.append(v)  
           
        return ''.join(stack)