#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking
for n-queens problem or a graph coloring problem.'''

# Python3 program for solution of M Coloring
# problem using backtracking


class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to check
	# if the current color assignment
	# is safe for vertex v
	def isSafe(self, v, colour, c):
		for i in range(self.V):
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True

	# A recursive utility function to solve m
	# coloring problem
	def graphColourUtil(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m + 1):
			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				if self.graphColourUtil(m, colour, v + 1) == True:
					return True
				colour[v] = 0

	def graphColouring(self, m):
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) == None:
			return False

		# Print the solution
		print("Solution exist and Following are the assigned colours:")
		for c in colour:
			print(c, end=' ')
		return True


# Driver Code
if __name__ == '__main__':
	g = Graph(4)
	g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
	m = 3

	# Function call
	g.graphColouring(m)


# In[3]:


'''program to solve N Queen Problem using Branch or Bound'''
import heapq

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens_branch_and_bound(n):
    min_heap = []  # Priority queue to process promising nodes

    def heuristic(board, row, n):
        # A heuristic to prioritize nodes
        # Here, we prioritize the placement of queens in the left-most columns
        return n - row

    # Initialize the priority queue with an empty board
    heapq.heappush(min_heap, (0, [-1] * n))

    while min_heap:
        (cost, board) = heapq.heappop(min_heap)
        row = board.index(-1)
        
        if row == n - 1:  # If all queens are placed, add the solution
            yield board
        else:
            for col in range(n):
                if is_safe(board, row, col, n):
                    new_board = board[:]
                    new_board[row] = col
                    new_cost = heuristic(new_board, row + 1, n)
                    heapq.heappush(min_heap, (new_cost, new_board))

def print_solutions(solutions, technique_name):
    if solutions:
        print(f"Solutions found using {technique_name}:")
        for idx, solution in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            for row in solution:
                print('.' * row + 'Q' + '.' * (len(solution) - row - 1))
            print()
    else:
        print(f"No solutions found using {technique_name}.")

n = 8  # Change 'n' to the desired board size
solutions_branch_bound = list(solve_n_queens_branch_and_bound(n))
print_solutions(solutions_branch_bound, "Branch and Bound")


# In[ ]:




