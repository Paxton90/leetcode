from typing import Optional
from utils import TreeNode, array_to_binary_tree

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.count = 0
        self.prefix_sum = {0: 1}
        def dfs(node: TreeNode, targetSum: int, curr_sum: int) -> None:
            if not node:
                return
            
            curr_sum += node.val
            self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
            self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1

            print(node.val, curr_sum, self.count, self.prefix_sum)
            
            dfs(node.left, targetSum, curr_sum)
            dfs(node.right, targetSum, curr_sum)

            
            self.prefix_sum[curr_sum] -= 1
            if self.prefix_sum[curr_sum] == 0:
                del self.prefix_sum[curr_sum]
        dfs(root, targetSum, 0)
        return self.count
        
    

    
def test():
    s = Solution()
    print(s.pathSum(array_to_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1]), 8))
    print(s.pathSum(array_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))