class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        curr = 0 if s[0] == '0' else 1

        for i in range(2, n+1):
            one_digit = int(s[i-1:i])
            two_digit = int(s[i-2:i])
            tmp = 0
            #one digit is valid
            if one_digit >= 1:
                tmp += curr
            #two digits are valid
            if 10<= two_digit <= 26:
                tmp += prev
            prev, curr = curr, tmp
        return curr
