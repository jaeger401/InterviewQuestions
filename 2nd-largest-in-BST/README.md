##2nd Largest Item in a Binary Search Tree

######Source: [interviewcake.com](https://www.interviewcake.com/question/second-largest-item-in-bst)

###The Problem

**Write a function to find the 2nd largest element in a binary search tree.**

Here's a sample binary tree node class:

```python
class BinaryTreeNode:

    def __init__ (self, value):
        self.value = value
        self.left =  None
        self.right = None

    def insert_left (self, value):
        self.left = BinaryTreeNode (value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode (value)
        return self.right
```

###My Solution (in 17 minutes)

Let's clarify some assumptions:

1. There is a function somewhere that handles the actual logic of inserting values into the BST properly. The class definition above doesn't do this.
2. The BST in question has at least two elements. Removing this restriction is easy to fix, but amounts to error-checking instead of solving the logic of the question.
3. The BST in question is a vanilla unbalanced tree. It's not an AVL tree, red-black tree, splay tree, or anything like that.
4. In the following examples, I'm going to use the elements of the set [1..10] as the values of my tree.

####Working Out The Logic

**First, find the largest element in the tree.**

The position of the largest element is going to be determined by the order in which it was added to the tree:

* If it was added first, it'll be the root of the tree. We'll know this because the root of the tree will have no right-hand child node.

![Largest as root](images/largest-root.png)

* Otherwise, it'll be the right-most node of the tree.
    * Wait...the right-most node has no right-hand child. Aha, that means that the first case above elides with this one!
    * *Therefore, the largest value is always the right-most node, which may be the root.* (Editor's note: Felt dumb for not remembering that straight off.)

(insert images here)

**Next, find the 2nd-largest element in relationship to the largest element.**

Thinking through where the 2nd-largest could be in the tree, I see the following cases:

1. At the root, if it's inserted first.
2. The parent of the largest element.
   * Wait, this is equivalent to the first case, because if it's the root, then by definition the only element in its right sub-tree would be the largest element.
3. The largest node of the left sub-tree of the largest node.

####The Algorithm

Given the logic as above, a quick pseudo-code algorithm would look like this:
```
largest = find_largest(tree)
if largest.left == nil
  then return parent  # Editor's note: I didn't take into consideration that the node doesn't have a link to its parent
  else return find_largest(largest.left)
```

On average, find_largest would run in O(log n) time.
The worst-case run time would be O(n) if the elements were inserted in ascending order.
Best-case, the results would come back in O(1) time, if the elements had been inserted in descending order.

###My code (in 13 more minutes)

It's hard to show an evolving though process in markdown. This is the final state of the implementation at the end of the remaining 13 minutes of this question.

```python
def insert(value, tree_node): # This is the missing insert function from above. Assume it's implemented.
  # Code goes here

def find_largest(tree_node):
"""Returns a tuple of (largest_node, parent_of_largest)"""
  if tree_node.right is None:
    return (tree_node, None)
  else:
    return (find_largest(tree_node.right), tree_node) # Editor's note: there's a big bug here; see code in repo for working example

def find_next_largest(tree_node):
  (largest, parent) = find_largest(tree_node)
  if largest.left is None:
    return parent
  else:
    (largest, parent) = find_largest(largest.left)
    return largest
```

