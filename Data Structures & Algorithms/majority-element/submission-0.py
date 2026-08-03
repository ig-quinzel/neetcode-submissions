from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=Counter(nums)
        maxx=0
        maxn=0
        n=len(nums)
        for key,val in ans.items():
            if val>(n//2) and val>maxx:
                maxx=val
                maxn=key
        return maxn

        