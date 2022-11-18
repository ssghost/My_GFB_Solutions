from typing import List, Tuple
class Solution:
    def walkstep(M: List[List[int]]) -> int:
        x, y = len(M), len(M[0])
        ptr = [0,0]
        passed = [[0,0]]
        spade = True
        cache, cachestep, cachespade = [], [], []
        step = 1
        def findnext(ptr: List[int], step: int, spade: bool) -> Tuple[List[int], int, bool]:
            possible = []
            udlr = [[ptr[0]-1,ptr[1]],[ptr[0]+1,ptr[1]],[ptr[0],ptr[1]-1],[ptr[0],ptr[1]+1]]
            for i in range(4):
                if spade:
                    if udlr[i][0] in range(x) and udlr[i][1] in range(y) and udlr[i] not in passed:
                        possible.append(udlr[i])
                else:
                    if udlr[i][0] in range(x) and udlr[i][1] in range(y) and udlr[i] not in passed:
                        if M[udlr[i][0]][udlr[i][1]] == 0:
                            possible.append(udlr[i])
            if len(possible) == 0:
                return cache.pop(), (cachestep.pop())+1, cachespade.pop()
            if len(possible) == 1:
                return possible[0], step+1, spade
            if len(possible) > 1:
                out = possible.pop()
                cache.extend(possible)
                cachestep.extend([step]*len(possible))
                cachespade.extend([spade]*len(possible))
                return out, step+1, spade
        while ptr[0] < x-1 or ptr[1] < y-1:
            ptr, step, spade = findnext(ptr, step, spade)
            if M[ptr[0]][ptr[1]] == 1:
                spade = False
            passed.append(ptr)
        return step
            
