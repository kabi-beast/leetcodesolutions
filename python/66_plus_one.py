class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        carry = (digits[i-1] + 1) // 10
        digits[i-1] = (digits[i-1] + 1) % 10
        i -= 2
        while carry and i >=0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits
