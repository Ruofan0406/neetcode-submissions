class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = {}
        for s in strs:
            sorts = "".join(sorted(s))
            if sorts not in ref:
                ref[sorts] = []
            ref[sorts].append(s)
        return list(ref.values())