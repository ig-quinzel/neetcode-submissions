class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w=min(strs,key=len)
        for i in range(len(w)):
            ch=w[i]
            for j in strs:
                if ch!=j[i]:
                    return w[:i]
        return w
