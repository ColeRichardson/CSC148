def insert_right(self, item: Any) -> None:
    """
    insert item as the right child of this tree.
    if a current right child exists, that child gets shifted down.
    one level and becomes the right chold of the newly inserted one.

    SOLUTIONS WILL BE POSTED
    :param self:
    :param item:
    :return:
    """

def __contains__(self, item: Any) -> bool:
    """
    return whether item is in this binary tree.

    :param self:
    :param item:
    :return:
    """
    #TODO complete this method recursively

    return self._key == item or \
        self._left != None and self._left.__contains__(item) or \
        self._right != None and self._right.__contains__(item)

"""
for tree traversals there is preorder: Root -> L -> R
inorder: L -> Root -> R
post order: L -> R -> Root
"""

def preorder(t: BinaryTree) -> list:
    """

    :param t:
    :return:
    """
     if not t:
         return []
     return[t.get_key()] + preorder(t.get_left)........

def string_expr(tree: BinaryTree):
    """

    :param tree:
    :return:
    """
    if isinstance(tree.get_key(), int):
        return (tree.get_key())

    return '(' + string_expr(tree.get_left()) + ')' + str(tree.get_key())......

# ahlan aamel eh: hello how are you ?

def find(self, data) -> BsTNode:

    def _find(node: _BSTNode, data: Any) -> BST_Node:  #this is a helper function only used by find so we keep it in find
        #base case
        .....

def insert(self, data: Any) -> None:
    """
    insert <item> into this BST, keeping the BST property
    :param self:
    :param item:
    :return:
    """
    # my solution
    if not self.root:
        self.root = BST_Node(data)
    elif item < self.root:
        self._left.insert(data)
    elif item > self.root:
        self._right.insert(data)

    """
    sadias solution
    """
    def_insert():
    ............
    if not node:
        # so ive reached a spot where i want my data to go
        #whay shoupd i do
        node = _BSTNode(data)
    if data < node.item:
        node.left = _insert

def height(self) -> int:
    """
     return height of this tree
    """
    def _height(node):
        """
        helper function for height. Reutnr height if tree rooted at node.
        A tree that only has one node (root) has height of 0
        a tree that is empty has a height of -1

        :param node:
        :return:
        """
        #complete this method recursively; max function might be useful
        # my solution
        if self.is_empty():
            return -1
        elif not self.left and not self.right:
            return 0
        else:
            height = 0
            if self.left:
                height += 1
        """
        sadias solution
        if not node:
            return -1
        return max(_height(node._left), ) ......
        """

    return _height(self.root)


