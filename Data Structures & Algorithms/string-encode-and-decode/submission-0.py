class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=str(len(i))
            ans+="#"
            ans+=i
        return ans
        
    def decode(self, s: str) -> List[str]:
        ans=[]
        new=""
        n=len(s)
        i=0
        while i<n:
            j=i
            while j<n and s[j]!="#":
                j+=1
            num=int(s[i:j])
            start=j+1
            new=s[start:start+num]
            ans.append(new)
            i=j+num+1
        return ans
            
                



