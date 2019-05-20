# import unittest
#
# class TestTreeNode(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.T = TreeNode(1)
#
#     def test_root_val(self):
#         self.assertEqual(self.T.val, 1)
#
#     def test_left_is_null(self):
#         self.assertIsNone(self.T.left)
#
#
# class TreeNode:
#
#     def __init__(self, val: int):
#         self.left = None
#         self.right = None
#         self.val = val
#
#
# def print_tree(T: TreeNode) -> str:
#     """
#     A function that returns the representation of a tree in string format
#     :param T: A instance of class TreeNode
#     :return: A string representation of T
#     """
#     current = T
#
#     return ''



class Vector(list):
    pass

    def __add__(self, other):
        return [a + b for a, b in zip(self, other)]


if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([2, 2, 3, 4])

    print(vector1 + vector2)