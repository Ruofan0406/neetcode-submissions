class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        clean = sorted(set(nums))

        length = 1
        max_length = 1

        for i in range(len(clean)-1):
            if clean[i] + 1 == clean[i+1]:
                length +=1
                max_length = max(length, max_length)
            else:
                length = 1
        
        return max_length if nums else 0



        