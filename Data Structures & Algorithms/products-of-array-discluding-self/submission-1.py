class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1 for _ in range(n)]
        suf=[1 for _ in range(n)]
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j]=suf[j+1]*nums[j+1]

        return [x*y for x,y in zip(pre,suf)]

