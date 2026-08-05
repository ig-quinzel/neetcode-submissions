class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<=1:
            return nums
        def merge(l,r):
            i=0
            j=0
            ans=[]
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    ans.append(l[i])
                    i+=1
                else:
                    ans.append(r[j])
                    j+=1
            while i<len(l):
                ans.append(l[i])
                i+=1
            while j<len(r):
                ans.append(r[j])
                j+=1
            return ans
        mid=n//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return merge(left,right)
        