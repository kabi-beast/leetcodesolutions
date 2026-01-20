class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k % (len(s))
        if k == 0:
            return s
        return s[k:] + s[:k]
        
