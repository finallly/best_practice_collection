class BinaryTree(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class MultiBinaryTree(object):

    def __init__(self, values, left=[], right=[]):
        self.values = values
        self.left = left
        self.right = right
