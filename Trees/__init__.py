import unittest


class TestTreeNode(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode(1)

    def test_root_val(self):
        self.assertEqual(self.root.val, 1)

    def test_left_is_null(self):
        self.assertIsNone(self.root.left)


class TreeNode:

    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val


if __name__ == '__main__':
    unittest.main()