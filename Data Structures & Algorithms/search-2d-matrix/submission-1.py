class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        t, b = 0, r-1

        while t <= b:
            mid = (t+b)//2
            if target > matrix[mid][-1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                break

        if t>b:
            return False

        row = (t+b)//2

        l, r = 0, c-1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid-1
            else:
                return True
        return False