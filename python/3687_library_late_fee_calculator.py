class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        pen = 0
        for day in daysLate:
            if day > 5:
                pen += 3 * day
            elif day >=2:
                pen += 2 * day
            else:
                pen += day
        return pen
        
