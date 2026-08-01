from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=defaultdict(int)
        for i in nums:
            ans[i]+=1
        new=[[] for _ in range(len(nums)+1)]
        for key,val in ans.items():
            new[val].append(key)
        fin=[]
        for i in range(len(new)-1,0,-1):
            for j in new[i]:
                fin.append(j)
                if len(fin)==k:
                    return fin



    