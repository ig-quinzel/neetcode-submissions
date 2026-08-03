class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=0
        w=0
        n=len(nums)
        while r<n:
            if nums[r]==val:
                r+=1
            else:
                nums[w]=nums[r]
                w+=1
                r+=1
        return w
