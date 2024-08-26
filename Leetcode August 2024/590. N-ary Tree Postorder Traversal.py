'''
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''
#Solution


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Initialize an empty list to store the result
        out = []
        # Start the traversal process
        self.traverse(root, out)
        # Return the final result
        return out
    
    def traverse(self, root, out):
        # Base case: If the root is None, return
        if not root:
            return None
        
        # Traverse each child of the current root in a recursive manner
        for c in root.children:
            self.traverse(c, out)
        
        # Append the value of the current root to the result list
        out.append(root.val)
    