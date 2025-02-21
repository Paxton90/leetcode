from typing import Optional
from utils import TreeNode, to_binary_tree


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def traverse(node, val):
            if not node: return
            self.visited.add(val)
            traverse(node.left, (2 * val) + 1)
            traverse(node.right, (2 * val) + 2)
        
        self.visited = set({})
        traverse(root, 0)

    def find(self, target: int) -> bool:
        return target in self.visited
    
def test():
    question_list = [
        [[[-1, None, -1]], [1], [2]],
        [[[-1, -1, -1, -1, -1]], [1], [3], [5]],
        [[[-1, None, -1, -1, None, -1]], [2], [3], [4], [5]]
    ]
    for question in question_list:
        ans = [None]
        tree = to_binary_tree(question[0][0])
        find_list = question[1:]
        s = FindElements(tree)
        for target in find_list:
            ans.append(s.find(target[0]))
        print(ans)