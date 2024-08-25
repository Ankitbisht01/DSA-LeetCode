'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
#Solution
class Solution:
    def __init__(self):
        self.postOrder = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.postOrder.append(root.val)
        return self.postOrder