"""
This file contains utility methods common for trees, particularly trees
"""
import math
import random
import time

from trees.tree import BinaryTreeNode

def get_mock_tree(size=10, balanced=True, height=3, complete=False):
    if height:
        size = 2 ** height

        if not complete:
            size = random.randint(size / 2, size - 1)

    root = BinaryTreeNode(value=0)
    nodes = [root]
    random.seed(time.clock())

    start = 1

    while start <= size:

        index = random.randint(0, len(nodes) - 1)
        node = nodes[index]

        while node.left and node.right:
            index = random.randint(0, len(nodes) - 1)
            node = nodes[index]

        is_left = random.choice([True, False])
        new_node = BinaryTreeNode(start)
        nodes.append(new_node)

        if is_left and not node.left:
            node.left = new_node
        elif not node.right:
            node.right = new_node
        else:
            node.left = new_node

        start += 1

    return root