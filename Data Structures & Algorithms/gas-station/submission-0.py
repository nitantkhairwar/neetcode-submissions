class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0

        for val in gas:
            totalGas += val
        
        for val in cost:
            totalCost += val
        
        if totalGas < totalCost:
            return -1
        
        start = 0
        CurrGas = 0

        for i in range(len(gas)):
            CurrGas += (gas[i] - cost[i])

            if CurrGas <0:
                CurrGas = 0
                start = i+1


        return start