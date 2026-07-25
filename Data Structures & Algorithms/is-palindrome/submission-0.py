class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        print(s)
        first = 0
        last = len(s)-1
        while first <= last:
            if s[first] == s[last]:
                last-=1
                first+=1
            else:
                return False
        return True
