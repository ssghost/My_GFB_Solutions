from typing import List
class Solution:
    def findTriple(l: List[int]) -> int:
        if len(l) < 3:
            return 0
        l.sort()
        out = 0
        for i in range(len(l)):
            for j in range(i,len(l)):
                for k in range(j, len(l)):
                    if l[j] % l[i] == 0 and l[k] % l[j] == 0:
                        out+=1
        return out

