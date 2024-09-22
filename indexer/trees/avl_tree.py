from typing import List, Optional, Any

from indexer.trees.bst_index import BinarySearchTreeIndex
from indexer.trees.avl_node import AVLNode


class AVLTreeIndex(BinarySearchTreeIndex):
    """
    An AVL Tree implementation of an index that maps a key to a list of values.
    AVLTreeIndex inherits from BinarySearchTreeIndex meaning it automatically
    contains all the data and functionality of BinarySearchTree.  Any
    functions below that have the same name and param list as one in 
    BinarySearchTreeIndex overrides (replaces) the BSTIndex functionality. 

    Methods:
        insert(key: Any, value: Any) -> None:
            Inserts a new node with key and value into the AVL Tree
    """
    
    def __init__(self):
       super().__init__()
       self.root: Optional[AVLNode] = None 
    
    def _height(self, node: Optional[AVLNode]) -> int:
        """
        Calculate the height of the given AVLNode.

        Parameters:
        - node: The AVLNode for which to calculate the height.

        Returns:
        - int: The height of the AVLNode. If the node is None, returns 0.
        """
        
        # TODO: make sure to update height appropriately in the
        # recursive insert function.
        
        if not node:
            return 0
        return node.height

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """
        Performs a right rotation on the AVL tree.

        Args:
            y (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root of the rotated subtree.
        """
        
        # TODO: implement the right rotation for AVL Tree

        # smaller than problem child and bigger than left child: left right rotation

        C = y.right 
        y.right = C.left
        C.left = y 

        # Update heights 
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        C.height = 1 + max(self._height(C.left), self._height(C.right))

        return C

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """
        Rotate the given node `x` to the left.
        Args:
            x (AVLNode): The node to be rotated.
        Returns:
            AVLNode: The new root of the subtree after rotation.
        """
        
        # TODO: implement the left rotation for AVL Tree

        # left child of x 
        A = x.left 
        # make right child of A the left child of x 
        x.left = A.right
        A.right = x 
        
        x.height = 1 + max(self._height(x.left), self._height(x.right)) 
        A.height = 1 + max(self._height(A.left), self._height(A.right))
        
        return A

    def _insert_recursive(self, current: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
        """
        Recursively inserts a new node with the given key and value into the AVL tree.
        Args:
            current (Optional[AVLNode]): The current node being considered during the recursive insertion.
            key (Any): The key of the new node.
            value (Any): The value of the new node.
        Returns:
            AVLNode: The updated AVL tree with the new node inserted.
        """
        # TODO: Implement a proper recursive insert function for an
        # AVL tree including updating height and balancing if a
        # new node is inserted.
        
        # TODO: Remove or comment out this line once you've implemented
        # the AVL insert functionality 
        # current = super()._insert_recursive(current, key, value)

        # return current
        # TODO: Implement a proper recursive insert function for an
        # AVL tree including updating height and balancing if a
        # new node is inserted.
        if not current:
            node = AVLNode(key)
            node.add_value(value)
            return node
        elif key < current.key:
            current.left = self._insert_recursive(current.left, key, value)
        elif key > current.key:
            current.right = self._insert_recursive(current.right, key, value)
        elif key == current.key:
            current.add_value(value)
        # return current_node

        # Check balance and perform rotations if necessary
        balance = abs(self._height(current.left) - self._height(current.right))

        # Left-Left Case
        if balance > 1 and key < current.left.key:
            return self._rotate_right(current)

        # Right-Right Case
        if balance > 1 and key > current.right.key:
            return self._rotate_left(current)

        # Left Right Case
        if balance > 1 and current.left.key < key < current.key:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)

        # Right Left Case
        if balance > 1 and current.key < key < current.right.key:
            current.right = self._rotate_right(current.right)  # check if the variables are stated properly
            return self._rotate_left(current)

        return current

    def insert(self, key: Any, value: Any) -> None:
        """
        Inserts a key-value pair into the AVL tree. If the key exists, the
         value will be appended to the list of values in the node. 

        Parameters:
            key (Any): The key to be inserted.
            value (Any): The value associated with the key.

        Returns:
            None
        """
        if self.root is None:
            self.root = AVLNode(key)
            self.root.add_value(value)
        else:
            self.root = self._insert_recursive(self.root, key, value)

    # def _inorder_traversal(self, current: Optional[AVLNode], result: List[Any]) -> None:
    #     if current is None:
    #         return
        
    #     self._inorder_traversal(current.left, result)
    #     result.append(current.key)
    #     self._inorder_traversal(current.right, result)
   
    # def get_keys(self) -> List[Any]:
    #     keys: List[Any] = [] 
    #     self._inorder_traversal(self.root, keys)
    #     return keys
