class BinaryTreeNode(object):
    """
    Represents a binary tree
    """

    def __init__(self, value):
        """
        Instantiates a tree node and stores the index `value` at the node
        :param value: The value to be stored at the node
        :return: None
        """

        self.value = value
        self.left = None
        self.right = None
