class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))

        while a <= b:
            a_sq = a * a
            b_sq = b * b

            if a_sq + b_sq == c:
                return True
            elif a_sq + b_sq < c:
                a += 1
            else:
                b -= 1

        return False