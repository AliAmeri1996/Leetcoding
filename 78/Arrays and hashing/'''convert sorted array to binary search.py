'''convert sorted array to binary search tree'''
'''The question says:

👉 You are given a sorted array (in ascending order).
👉 You need to turn it into a height-balanced binary search tree (BST).

BST property: left subtree values < root < right subtree values.

Height-balanced: for every node, the left and right subtrees’ heights differ by at most 1.

The trick:

Pick the middle element as root → keeps tree balanced.

Recursively do the same for left half (becomes left subtree) and right half (becomes right subtree).'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        root = TreeNode(nums[mid])
        root.left = build(lo, mid - 1)
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(nums) - 1)
