from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i<len(g) and j <len(s):
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count

if __name__ == "__main__":
    s = Solution()
    a = [1,2,3]
    b = [2,2]
    print(s.findContentChildren(a,b))