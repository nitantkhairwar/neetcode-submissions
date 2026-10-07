class Solution:
    def checkValidString(self, s: str) -> bool:
        maximum = 0
        minimum = 0
        for char in s:
            if char == "(":
                minimum += 1
                maximum += 1
            elif char == ")":
                minimum -= 1
                maximum -= 1
            else:
                minimum -= 1
                maximum += 1
            
            minimum = max(0, minimum)
            if maximum <0:
                return False
        return minimum == 0