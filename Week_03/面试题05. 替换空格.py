class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for char in s:
            res += r'%20' if char == ' ' else char
        return res    