class Solution:
    def pellets(self, p: str) -> int:
        p = int(p)
        if p in [0,1]:
            return 0
        if p % 2 == 0:
            return len(str(bin(p)))-1
        else:
            return len(str(bin(p)))
