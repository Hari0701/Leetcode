class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        costs.sort(key = lambda cost: cost[0] - cost[1])
        for i in range(len(costs)):
            ans += costs[i][0] if i < len(costs)/2 else costs[i][1]
        return ans    