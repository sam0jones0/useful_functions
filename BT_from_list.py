"""Function to create a binary tree from a provided list of values. List of values is expected
to be in the format found in most binary tree LeetCode questions.
"""


from collections import deque
from typing import List, Optional

from binary_tree import TreeNode


def gen_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """Returns root `TreeNode` of tree built using ``vals``, or `None` if no tree can be built.

    Args:
        vals: List of `int` or `None` vals in format [5,4,8,11,None,13,4,7,2,None,None,None,1].
    """
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])

    idx = 1
    while queue and idx < len(vals):
        node = queue.popleft()
        if vals[idx]:
            left = TreeNode(vals[idx])
            node.left = left
            queue.append(left)
        idx += 1
        if idx < len(vals) and vals[idx]:
            right = TreeNode(vals[idx])
            node.right = right
            queue.append(right)
        idx += 1

    return root
