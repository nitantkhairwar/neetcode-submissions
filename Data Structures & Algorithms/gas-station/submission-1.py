class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0

        for val in cost:
            totalCost += val
        
        for g in gas:
            totalGas +=g
        
        # No Solution
        if totalCost > totalGas:
            return -1
        
        #unique Solution

        CurrGas =0
        start =0

        for i in range(len(gas)):
            CurrGas += (gas[i] - cost[i])

            if CurrGas < 0:
                CurrGas = 0
                start = i+1
        return start
