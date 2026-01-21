# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        check = (high+low) // 2
        while(not(isBadVersion(check) and not isBadVersion(check-1))):
            print("in " + str(check))
            if isBadVersion(check):
                high = check - 1
            else:
                low = check + 1
            check = (high+low) // 2
        return check
        
