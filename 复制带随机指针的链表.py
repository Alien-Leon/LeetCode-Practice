"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copy(self, node):
        return Node(node.val, node.next, node.random)

    """
    解法一： 利用map记录拷贝后的node节点，并再一次遍历将复制后的节点中的next,random指针指向拷贝后节点
    解法二： 在每个节点后插入拷贝节点，随后对拷贝节点复制random指针指向，最后将链表拆分，可以达到不适用额外空间的效果。
    详见https://blog.csdn.net/qq_41855420/article/details/87893486
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_list = {}
        h = head
        while head:
            node_list[id(head)] = self.copy(head)
            head = head.next
        
        print(node_list)

        for k, v in node_list.items():
            if v.next:
                v.next = node_list[id(v.next)]
            if v.random:
                v.random = node_list[id(v.random)]
        if h:
            return node_list[id(h)]
        return None
