from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def array_to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()

def binary_tree_to_array(root: TreeNode) -> list[int]:
    """Convert a binary tree to a list representation."""
    if not root:
        return []
    
    result = []
    queue = [(root, 0)]  # (node, index)
    
    while queue:
        node, index = queue.pop(0)
        
        if node:
            # Ensure the list is large enough
            if index >= len(result):
                result.extend([None] * (index - len(result) + 1))
            
            result[index] = node.val
            queue.append((node.left, 2 * index + 1))
            queue.append((node.right, 2 * index + 2))
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result