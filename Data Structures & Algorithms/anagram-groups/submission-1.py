from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            new="".join(sorted(i))
            ans[new].append(i)
        anss=[]
        for i in ans.values():
            anss.append(i)
        return anss
        