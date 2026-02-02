class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map = {}
        map[0] = 0
        map[1] = 1
        map[6] = 9
        map[8] = 8
        map[9] = 6
        print(digits)
        i = 0
        j = len(num) - 1
        while i <= j:
            n1 = int(num[i])
            n2 = int(num[j])
            if (n1 in map) and (n2 in map) and (n1 == map[n2]):
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
