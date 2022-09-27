from typing import List, Dict
class Solution:
    def sorting(l: List[str]) -> List[str]:
        sortdict = {}
        level = len(l)
        lendict = {}
        for i,v in enumerate(l):
            sortdict[i] = list(v.split('.'))
            for n in sortdict[i]:
                sortdict[i][n] = int(sortdict[i][n])
            if len(sortdict[i]) not in lendict.keys():
                lendict[len(sortdict[i])] = sortdict[i][-1]
            elif sortdict[i][-1] > lendict[len(sortdict[i])]:
                lendict[len(sortdict[i])] = sortdict[i][-1] 
        for le in list(set(range(max(lendict.keys())+1)) - set(lendict.keys())):
            lendict[le] = 0
        lendict = dict(sorted(lendict.items, key = lambda x: x[0]))
        for k in range(1,max(lendict.keys())+1):
            lendict[k] = lendict[k-1]
        lendict.pop(0)
        def sortmeth(li: List[int], level: int, lendict: Dict[int,int]) -> int:
            sout = 0
            for m in range(len(li)):
                sout += (lendict[m+1]*level*m + li[m])
            return sout        
        sortdict = dict(sorted(sortdict.items(), key = lambda x: sortmeth(x[1], level, lendict)))
        out = [""]*level
        for i,v in enumerate(sortdict.keys()):
            out[i] = l[v]
        return out
