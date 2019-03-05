# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
import ast
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = queue.Queue()
        q.put(root)
        l = []
        while not q.empty():
            node = q.get()
            if node:
                l.append(node.val)
                q.put(node.left)
                q.put(node.right)
            else:
                l.append(None)
        i = len(l)-1
        while i > 0 and l[i] is None:
            i -= 1
        return str(l[:i+1])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def node_join(i, data):
            if i >= len(data):
                return None
            else:
                node = TreeNode(data[i])
                node.left = node_join(i*2 + 1, data)
                node.right = node_join(i*2 + 2, data)
                return node
                
        return node_join(0, ast.literal_eval(data))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))