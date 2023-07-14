class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distributeCoins(root) -> int:
    global move 
    move = 0

    def dfs(root):
        global move
        leftmove = 0
        rightmove = 0

        if root is None:
            return 0
        
        # 看左右子树多余的硬币
        if root.left is not None:
            leftmove = dfs(root.left)
        
        if root.right is not None:
            rightmove = dfs(root.right)

        move = move + abs(leftmove) + abs(rightmove)

        # 返回多余的硬币数
        return root.val + leftmove + rightmove - 1
    
    dfs(root)
    return move

def construct_tree(a):
    nodes = [None] + [TreeNode(i) if i != -1 else None for i in a ]

    for i in range(1, len(nodes) // 2):
        if nodes[i] is None:
            continue
        leftidx = i * 2
        rightidx = i * 2 + 1

        if leftidx < len(nodes):
            nodes[i].left = nodes[leftidx]
        
            if rightidx < len(nodes):
                nodes[i].right = nodes[rightidx]

    return nodes[1]

a = [1,0,0,-1,3]
root = construct_tree(a)
# print(root.val, root.left.val, root.right.val)
print(distributeCoins(root))