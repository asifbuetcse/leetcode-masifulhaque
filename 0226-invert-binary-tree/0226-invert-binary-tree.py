# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def switch(head):
            if (head!= None and (head.left != None or head.right != None)):
                (head.left, head.right) = (head.right, head.left)
                switch(head.left)
                switch(head.right)
            else:
                return;
        
        switch(root)    
        return root
        