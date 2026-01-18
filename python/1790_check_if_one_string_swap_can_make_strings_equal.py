class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first = []
        second = []
        unequal = 0
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                print(s1[i])
                print(s2[i])
                print("---------")
                unequal += 1
                first.append(s1[i])
                second.append(s2[i])
        if unequal == 0:
            return True
        if unequal == 2:
            if first[0] == second[1] and first[1] == second[0]:
                return True
        return False
        
