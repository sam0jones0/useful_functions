from typing import Any, List, Tuple


class TreeNode:
    """Simple binary tree."""

    def __init__(self, root_obj: Any) -> None:
        self.val = root_obj
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)

    def insert_left(self, new_node: "TreeNode") -> None:
        """Inserts a left child node under this current node."""
        if self.left is None:
            self.left = TreeNode(new_node)
        else:
            new_child = TreeNode(new_node)
            new_child.left = self.left
            self.left = new_child

    def insert_right(self, new_node: "TreeNode") -> None:
        """Inserts a right child node under this current node."""
        if self.right is None:
            self.right = TreeNode(new_node)
        else:
            new_child = TreeNode(new_node)
            new_child.right = self.right
            self.right = new_child

    def display(self) -> None:
        """Prints a string representation of the tree with this node as the root."""
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self) -> Tuple[List[str], int, int, int]:
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
