"""
 Path Finding Algorithm to move from source to destination - Move Left or right 

"""

def path_finder(matrix, position, destination):
	if (destination-1, destination-1) == position:
		return [(position, position)]
	x, y = position

	# check for left
	if x+1 < destination and matrix[x+1][y] == 1:
		res1 = path_finder(matrix, (x+1, y), destination)
		if res1 != None:
			# If exist print the current coordinates and the result
			return [(x,y)] + res1

	# check for down
	if y+1 < destination and matrix[x][y+1] == 1:
		res2 = path_finder(matrix, (x, y+1), destination)
		if res2 != None:
			return [(x,y)] + res2


maze = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]
print path_finder(maze, (0,0) , 3)