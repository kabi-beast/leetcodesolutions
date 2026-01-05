class Solution:
    def largestEven(self, s: str) -> str:
        s_list = list(s)
        i = len(s) - 1
        while i >= 0 and int(s_list[i]) == 1:
            i -= 1
        print(len(s) - 1)
        print(i)
        return s[:i + 1]
        
