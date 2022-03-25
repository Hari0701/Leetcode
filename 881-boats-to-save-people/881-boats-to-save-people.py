class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people) - 1
        people.sort()
        boats = 0
        while(i <= j):
            boats += 1
            if(people[i] + people[j] <= limit):
                i = i + 1
            j = j - 1    
        return boats    