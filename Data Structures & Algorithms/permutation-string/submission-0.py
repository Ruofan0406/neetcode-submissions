class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        l=0

        for r in range(len(s2)):
            if sorted(s2[l:l+length]) == sorted(s1):
                return True
            else:
                l+=1
        return False