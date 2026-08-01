class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        n=len(nums)
        for i in range(n):
            x=target-nums[i]
            if x not in ans:
                ans[nums[i]]=i
            else:
                return sorted(list((i,ans[x])))
        