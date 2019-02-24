# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的最长路径与之解法类似

class Solution:
    def __init__(self):
        self.result = -1<<31
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        def dfs(root):
            """'
            若一个节点是最大路径和中的节点，那么这个节点对应的路径有以下情况:
                node            node        node            node
                / \             /               \
            left   right      left              right
            """

            if root:
                # 判断左右子树的数值是否能使和更大
                left_val = max(0, dfs(root.left))   
                right_val = max(0, dfs(root.right))
                self.result = max(self.result, root.val + left_val + right_val)
                # 判断单节点值还是携带子树的值有效
                return max(root.val, root.val + max(left_val, right_val))
            else:
                return -99999
        dfs(root)
        return self.result


root = TreeNode(-2)
# left = TreeNode(-1)
# right = TreeNode(3)
# root.left = left
# root.right = right


s = Solution()
print(s.maxPathSum(root))

