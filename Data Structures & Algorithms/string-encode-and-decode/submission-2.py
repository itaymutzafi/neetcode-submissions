class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # i is the left pointer, and j is the right pointer
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i: j]) #this is all the length encoded int
            i = j + 1 # jump to the char after # (included in the slicing)
            j = i + length # the end of the string (index of the start of the next length, excluded in slicing)
            res.append(s[i:j])
            i = j # jump the left pointer to the start of the length of the next string

        return res

            
