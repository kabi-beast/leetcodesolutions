class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        map = {}
        for i in range(1, len(nums) + 1):
            map[i] = 0
        for num in nums:
            map[num] = map[num] + 1
        for key in map.keys():
            if map[key] == 0:
                res.append(key)
        return res
        
