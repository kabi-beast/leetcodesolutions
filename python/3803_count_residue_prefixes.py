class Solution:
    def residuePrefixes(self, s: str) -> int:
        count = 0
        map = {}
        length = 0
        for char in s:
            print(char)
            length += 1
            map[char] = 1
            if  length % 3 == len(map.keys()) :
                count += 1
        return count
        
