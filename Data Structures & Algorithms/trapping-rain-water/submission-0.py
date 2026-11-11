class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftmax = [0]*length
        rightmax = [0]*length

        if length == 0: return 0

        leftmax[0] = height[0]

        for i in range(1, length):
            leftmax[i] = max(leftmax[i-1], height[i])

        rightmax[length-1] = height[length-1]

        for i in range(length-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])

        res = 0

        for i in range(length):
            res += min(leftmax[i], rightmax[i]) - height[i]

        return res

