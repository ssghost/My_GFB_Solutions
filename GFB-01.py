class Solution:
    def encode(self, s: str) -> str:
        chalist = list("thequickbrownfoxjumpsoverthelazydog")
        binbase  = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
        binlist = [binbase[i*6:i*6+6] for i in range(int(len(binbase)/6))]
        binlist.pop(0)
        while "000000" in binlist:
            binlist.remove("000000")
        mydict = {}
        for j in range(len(chalist)):
            mydict[chalist[j]] = binlist[j]
        mydict[' '] = "000000"
        mydict['A'] = "000001" 
        if ord(s[0]) in range(65, 91):
            s = 'A'+ chr(ord(s[0])+32) + s[1:]
        out = ""
        for c in s:
            out+= mydict[c]
        return out
        