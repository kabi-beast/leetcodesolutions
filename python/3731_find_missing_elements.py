class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        start = nums[0]
        result = []
        for i in range(1, len(nums)):
            while nums[i] != (start + 1):
                result.append(start + 1)
                start += 1
            else:
                start += 1
        return result
