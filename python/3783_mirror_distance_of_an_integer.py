class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        rev_s = s[::-1]
        print(rev_s)
        rev_n = int(rev_s)
        return abs(n - rev_n)
        
