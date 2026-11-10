class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = defaultdict(list)
        for s in strs:
            sorts = "".join(sorted(s))
            ref[sorts].append(s)
        return list(ref.values())