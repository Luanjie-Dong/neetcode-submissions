class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(x)}#{x}" for x in strs])

    def decode(self, s: str) -> List[str]:
        res , i = [] , 0

        while i < len(s):
            seperator = s.index("#",i)
            length = int(s[i:seperator])
            decoded = s[seperator+1:seperator+length+1]
            res.append(decoded)

            i = seperator+length+1
        return res
        



        