from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=0
        c=0
        for i in nums:
            if c==0:
                c+=1
                maj=i
            elif maj==i:
                c+=1
            else:
                c-=1
        return maj

        