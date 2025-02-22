from typing import Optional
from utils import TreeNode, array_to_binary_tree


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ...


def test():
    s = Solution()
    print(s.longestZigZag(array_to_binary_tree([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])))
    print(s.longestZigZag(array_to_binary_tree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])))