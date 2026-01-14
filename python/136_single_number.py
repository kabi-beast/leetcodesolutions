class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        sum = 0
        for num in nums:
            if num in map:
                sum -= num
            else:
                sum += num
                map[num] = 1
        return sum
        
