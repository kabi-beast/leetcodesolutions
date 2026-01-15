class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        map = {}
        for num in nums:
            if num in map:
                map[num] = map[num] + 1
            else:
                map[num] = 1
            if map[num] > threshold:
                return num
        
