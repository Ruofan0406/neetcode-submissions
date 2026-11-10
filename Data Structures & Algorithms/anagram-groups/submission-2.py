class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = defaultdict(list)
        for s in strs:
            temp = [0]*26
            for c in s:
                temp[ord(c)-ord('a')] += 1
            ref[tuple(temp)].append(s)
        return list(ref.values())
