from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                ans += "1"
            else:
                ans += "0"
        return ans
        

def test():
    s = Solution()
    print(s.findDifferentBinaryString(["01","10"]))
    print(s.findDifferentBinaryString(["00","01"]))
    print(s.findDifferentBinaryString(["111","011","001"]))
