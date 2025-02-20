import math

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        leftover = money - children
        if leftover < 0: return -1

        count = math.floor(leftover / 7)
        if money == 8 * children - 4:
            count -= 1
        if money > 8 * children:
            count = children - 1
        return count

def test():
    s = Solution()
    print(s.distMoney(20, 3))
    print(s.distMoney(16, 2))
    print(s.distMoney(1, 2))
    print(s.distMoney(4, 1))