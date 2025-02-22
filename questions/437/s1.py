from typing import Optional
from utils import TreeNode, array_to_binary_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        def dfs(root, target):
            if root is None: return
            find_sum_from_node(root, target)
            dfs(root.left, target)
            dfs(root.right, target)
        
        def find_sum_from_node(node, target):
            if node is None: return
            if node.val == target: self.result += 1
            find_sum_from_node(node.left, target-node.val)
            find_sum_from_node(node.right, target-node.val)
        
        dfs(root, targetSum)
        return self.result
    
def test():
    s = Solution()
    print(s.pathSum(array_to_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1]), 8))
    print(s.pathSum(array_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))