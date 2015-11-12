#!/usr/bin/env python
"""
FILE:   2nd-largest.py
AUTHOR: jaeger401
DATE:   Wed Nov 11 15:44:57 EST 2015
DESCR:  Python implementation of interviewcake.com coding question
"""

# The initial BST implementation, as given
class BinaryTreeNode:

    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left (self, value):
        self.left = BinaryTreeNode (value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode (value)
        return self.right

# The remainder is my code. 
# Yes, right out of my own little brain, no Google required.

    def insert(self, value): 
        """Inserts a value into its proper place in the binary tree."""
        if value < self.value:
            if self.left is not None:
                return self.left.insert(value)
            else: 
                return self.insert_left(value)
        else:
            if self.right is not None:
                return self.right.insert(value)
            else:
                return self.insert_right(value)

    def print_inorder_traversal(self):
        """Prints the values in the tree, using in-order traversal"""
        if self.left is not None:
            self.left.print_inorder_traversal()
        print "%s " % self.value,
        if self.right is not None:
            self.right.print_inorder_traversal()

    def print_preorder_traversal(self):
        """Prints the values in the tree, using pre-order traversal"""
        print "%s " % self.value,
        if self.left is not None:
            self.left.print_preorder_traversal()
        if self.right is not None:
            self.right.print_preorder_traversal()


def find_largest(tree_node):
    """Takes a BST and returns a tuple of (largest_node, parent_of_largest)"""
    if tree_node.right is None: 
        # Largest element is the root
        return (tree_node, None)
    else:
        # I messed this up in the first pass. It returned a massively
        # nested tuple of garbage.
        ## return (find_largest(tree_node.right), tree_node) 

        # This is better
        if tree_node.right.right is None:
            return (tree_node.right, tree_node)
        else:
            return find_largest(tree_node.right)


def find_next_largest(tree_node):
    largest, parent = find_largest(tree_node)
    if largest.left is None:
        return parent.value
    else:
        largest, parent = find_largest(largest.left)
    return largest.value


def tree_from_array(numbers):
    """Takes a list of numbers and returns a BST"""
    tree = None
    for i in numbers:
        if tree is None:
            tree = BinaryTreeNode(i)
        else:
            tree.insert(i)
    return tree


if __name__ == "__main__":
    tree = tree_from_array([5,6,4,2,9,8,4])
#    tree.print_inorder_traversal()
#    print
#    tree.print_preorder_traversal()
#    print
    print find_next_largest(tree) == 8

    tree = tree_from_array([8, 9, 10])
    print find_next_largest(tree) == 9

    tree = tree_from_array([10, 9, 8])
    print find_next_largest(tree) == 9

    tree = tree_from_array([10, 8, 9])
    print find_next_largest(tree) == 9

    tree = tree_from_array([9, 8, 10])
    print find_next_largest(tree) == 9

    tree = tree_from_array([1, 7, 5, 10])
    print find_next_largest(tree) == 7

    tree = tree_from_array([1, 4, 2, 3, 7, 5, 9, 10, 8, 6])
    print find_next_largest(tree) == 9

    tree = tree_from_array([10, 10, 9])
    print find_next_largest(tree) == 10

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
