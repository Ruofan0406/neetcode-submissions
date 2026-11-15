class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = 0
        needcount = len(need)

        res = [-1,-1]
        minlen = float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and need[c] == window[c]:
                have += 1

            while have == needcount:
                if r-l+1 < minlen:
                    minlen = r-l+1
                    res = [l, r]

                leftchar = s[l]
                window[leftchar] -= 1

                if leftchar in need and window[leftchar] < need[leftchar]:
                    have -= 1
                
                l += 1

        l, r = res

        return s[l:r+1] if minlen != float("inf") else ""