from typing import Optional
from utils import TreeNode, binary_tree_to_array


class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        index = 0

        def dfs(depth=0):
            nonlocal index
            entry_index = index
            
            count = 0
            while index < len(s) and s[index] == '-':
                count += 1
                index += 1
            if count != depth:
                index = entry_index
                return None
            
            num = 0
            while index < len(s) and s[index].isdigit():
                num = num * 10 + int(s[index])
                index += 1
            
            node = TreeNode(num)
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node
        
        return dfs()
        
def test():
    s = Solution()
    print(binary_tree_to_array(s.recoverFromPreorder("1-2--3--4-5--6--7")))
    print(binary_tree_to_array(s.recoverFromPreorder("1-2--3---4-5--6---7")))
    print(binary_tree_to_array(s.recoverFromPreorder("1-401--349---90--88")))