class Solution:

    def findOriginal(self, leftNumber, rightNumber, original):
        i = 0
        leftIndex = 0
        rightIndex = 0
        while(i < len(original)):
            if original[i] == leftNumber:
                leftIndex = i
            if original[i] == rightNumber:
                rightIndex = i
        
        return [leftIndex, rightIndex]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = nums
        nums.sort()
        left = 0
        right = len(nums) - 1
        while(nums[right] > target):
            right = right - 1
        while(left < len(nums) and nums[left] < target and right >=0):
            if (nums[left] + nums[right] == target):
                return self.findOriginal(nums[left], nums[right], original)
            elif (nums[left] + nums[right] > target):
                right = right - 1
            else:
                left = left + 1
