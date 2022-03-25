class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if(len(tops) == len(bottoms)):
            t_freq = {}
            b_freq = {}
            for v in tops:
                if v in t_freq:
                    t_freq[v] += 1
                else:
                     t_freq[v] = 1
            for v in bottoms:
                if v in b_freq:
                    b_freq[v] += 1
                else:
                     b_freq[v] = 1  
                        
            def get_key(my_dict ,val):
                for key, value in my_dict.items():
                    if val == value:
                        return key    
                    
            if max(t_freq.values()) > max(b_freq.values()):
                val =  get_key(t_freq,max(t_freq.values()))
                idx = []
                counter = 0
                for i in range(len(tops)):
                    if val != tops[i]:
                        idx.append(i)
                        
                for i in idx:
                    if(bottoms[i] == val):
                        tops[i] = bottoms[i]
                        counter += 1        
                    else: 
                        return -1
                return counter    
            else: 
                val = get_key(b_freq,max(b_freq.values()))
                idx = []
                counter = 0
                for i in range(len(bottoms)):
                    if val != bottoms[i]:
                        idx.append(i)
                        
                for i in idx:
                    if(tops[i] == val):
                        bottoms[i] = tops[i]
                        counter += 1        
                    else: 
                        return -1
                return counter    
        else: 
            return -1