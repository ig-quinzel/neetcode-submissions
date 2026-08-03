class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            pro=1
            for j in range(n):
                if i!=j:
                    pro*=nums[j]
            ans.append(pro)
        return ans
            
