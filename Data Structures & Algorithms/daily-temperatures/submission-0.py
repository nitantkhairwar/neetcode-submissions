class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        result = [0]*n
        stack = []

        for i, t in enumerate(temps):
            while stack and stack[-1][0]< t:
                temp, indx = stack.pop()
                result[indx] = i - indx
            stack.append((t, i))
        return result

