#!/usr/bin/env python
# coding: utf-8

# In[2]:


''' Implement Alpha-Beta Tree search for any game search problem.'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_game_tree():
    # Define a sample game tree with values
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(6)
    node3 = TreeNode(9)
    node4 = TreeNode(2)
    node5 = TreeNode(7)
    node6 = TreeNode(4)
    node7 = TreeNode(10)

    root.children = [node1, node2]
    node1.children = [node3, node4]
    node2.children = [node5, node6]
    node4.children = [node7]

    return root

def alpha_beta_search(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_search(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_search(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

def main():
    game_tree = build_game_tree()
    depth = 7
    result = alpha_beta_search(game_tree, depth, float('-inf'), float('inf'), True)
    print("Optimal value:", result)

if __name__ == "__main__":
    main()


# In[ ]:




