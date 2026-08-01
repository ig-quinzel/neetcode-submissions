from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd=defaultdict(int)
        td=defaultdict(int)
        for i in s:
            sd[i]+=1
        for j in t:
            td[j]+=1
        return sd==td

        
        