class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        a = 1
        b = 0
        for i in str_n:
            c = int(i)
            a *= c
            b += c
        return a - b