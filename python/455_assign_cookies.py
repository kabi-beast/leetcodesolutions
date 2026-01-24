class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        child = 0
        for cookie in range(len(s)):
            if child < len(g) and s[cookie] >= g[child]:
                child += 1
                result += 1
        return result
        
