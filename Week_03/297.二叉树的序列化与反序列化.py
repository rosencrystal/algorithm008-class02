#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 第一遍：前序遍历
class Codec:
    def __init__(self):
        self.vals = []
        self.root = None

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(alist):
            if alist[0] == 'None':
                alist.pop(0)
                return None
            root = TreeNode(alist[0])
            alist.pop(0)
            root.left = dfs(alist)
            root.right = dfs(alist)
            return root

        if data:
            self.vals = data.split(',')
            self.root = dfs(self.vals)    

        return self.root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

