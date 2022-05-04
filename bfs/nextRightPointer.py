class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def __repr__(self) -> str:
        return '%s -> n %s' % (self.val, self.next if self.next else None)
        
def connect(root):
    if not root: return None       
    q = [root]

    while q:
        node = q.pop(0)
        print(node)
        if node.left and node.right:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            q.append(node.right)
            q.append(node.left)

    return root
        



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2, Node(4),Node(5))
    root.right = Node(3, Node(6), Node(7))

    connect(root)
    

    
    
