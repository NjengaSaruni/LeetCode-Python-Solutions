import unittest

class TestTreeNode(unittest.TestCase):

    def setUp(self) -> None:
        self.T = TreeNode(1)

    def test_root_val(self):
        self.assertEqual(self.T.val, 1)

    def test_left_is_null(self):
        self.assertIsNone(self.T.left)


class TreeNode:

    def __init__(self, val: int):
        a = ''
        self.left = None
        self.right = None
        self.val = val


def print_tree(T: TreeNode) -> str:
    """
    A function that returns the representation of a tree in string format
    :param T: A instance of class TreeNode
    :return: A string representation of T
    """
    current = T

    return ''

if __name__ == '__main__':
    unittest.main()
    print_tree(TreeNode(4))