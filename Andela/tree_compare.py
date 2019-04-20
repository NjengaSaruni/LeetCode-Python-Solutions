import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(unittest.TestCase):
    def test_should_return_true_for_equal_nodes(self):
        self.assertTrue(compare(a_node, b_node))

    def test_should_return_false_for_non_equal_nodes(self):
        self.assertFalse(compare(a_node, c_node))

import collections


# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise
# def compare(a, b):
#     # Use iterative approach, O(number of nodes in larger tree) space and O(number of nodes in larger tree) time
#     # Recursive solution is more intuitive but have worse space complexity
#     # because of the recursive call stack
#
#     # Create a queue for each tree
#     queue_a = collections.deque([a.val])
#     queue_b = collections.deque([b.val])
#
#     # Iterate while items in stack
#     while queue_a and queue_b:
#
#         # Pop stack and compare if values are equal
#         if queue_a.pop() == queue_b.pop():
#
#             # Append corresponding values in tree
#             if a.left and b.left:
#                 queue_a.append(a.left.val)
#                 queue_b.append(b.left.val)
#
#             # If one tree is left-heavy, trees are not equal
#             elif a.left or b.left:
#                 return False
#
#             # Append corresponding right values in tree
#             if a.right and b.right:
#                 queue_a.append(a.right.val)
#                 queue_b.append(b.right.val)
#
#             # If one tree is right-heavy, trees are not equal
#             elif a.right or b.right:
#                 return False
#
#         else:
#             return False
#
#     return True

def compare(a, b):
    if a and b:
        if a.val == b.val:
            return compare(a.left, b.left) and compare(a.right, b.right)
    elif a or b:
        return False
    else:
        return True

    return False

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)
