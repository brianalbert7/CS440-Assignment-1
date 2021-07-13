import numpy as np
# from numpy import genfromtext

class Stack: 
	def __init__():
		self.stack = []

	def empty():
		return self.stack == []

	def next(): 
		val = self.stack[0]
		self.stack = self.stack[1:]
		return val

	def add(x):
		self.stack.append(x)

def general_tree_search(start, goal, cost, heuristic, datastructure):
	pass


def run_solver(start, goal, maze, algo):
	pass

def maze_parser(maze_filename: str, maze_size: int) -> np.ndarray:
	with open(maze_filename, 'r') as file:
		parsed_maze = [[int(n) for n in line.split(' ')[:3]] for line in file]


	maze = np.zeros((maze_size, maze_size))
	for square in parsed_maze:
		x = square[0]
		y = square[1]
		blocked = square[2]

		maze[x, y] = blocked


	import pdb
	pdb.set_trace()
	# maze = genfromtext(maze_filename, delimeter =' ')
		#location of obstacles
		#list -- [x pos, y pos, blocked]

	#2D list -- map[x, y] = 1 if blocked else 0
	return maze

def display_solution(maze, path): 
	#Use matplotlib
	pass

def run_single_problem(problem_file: str):
	with open(problem_file, 'r') as file:
		lines = [line for line in file]
	maze_size = int(lines[0])
	split_line_1 = lines[1].split(' ')
	start_pos = [int(split_line_1[0]), int(split_line_1[1])]
	split_line_2 = lines[2].split(' ')
	goal_pos = [int(split_line_2[0]), int(split_line_2[1])]
	algorithm = int(lines[3])
	maze_filename = 'mazes/maze_' + lines[4][0:3] + '.txt'

	maze = maze_parser(maze_filename, maze_size)
	run_solver(start, goal, maze, algorithm)


def runs_multiple_problems(problem_file: str):
	#iterate over all mazes
	pass

run_single_problem('problem.txt')