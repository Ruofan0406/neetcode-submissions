class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        whole = 1
        cnt = 0
        res = [0]*len(nums)
        position = 0
        for i, n in enumerate(nums):
            if n == 0:
                position = i
                cnt += 1
            else:
                whole *= n
        
        if cnt > 1:
            return res
        elif cnt == 1:
            res[position] = whole
            return res
        else:
            for i in range(len(nums)):
                res[i] = whole//nums[i]

        return res