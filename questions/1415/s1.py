import math


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = ""
        total = 3 * (2 ** (n-1))
        group = total / 3

        if k > total: return ans
        
        ans += chr(96 + math.ceil(k / group))

        prev_char = ans
        while group != 1:
            k = (k - 1) % group + 1
            group = group / 2
            
            min_c, max_c = self.get_min_max(prev_char)
            cur_char = max_c if k > group else min_c

            ans += cur_char
            prev_char = cur_char
        return ans
    
    def get_min_max(self, char):
        if char == "a": return "b", "c"
        elif char == "b": return "a", "c"
        elif char == "c": return "a", "b"

def test():
    s = Solution()
    print(s.getHappyString(1, 3))
    print(s.getHappyString(1, 4))
    print(s.getHappyString(3, 9))
    print(s.getHappyString(10, 100))
