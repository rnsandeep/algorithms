# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
# are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum 
# area is 0.)
#
# Sample input:
#
a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Expected output: 
# 6

def getNeighbours(i, j, a):
    neighbours =  [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
    neighbours = [n for n in neighbours if n[0] >=0 and n[0] < len(a) and n[1] >=0 and n[1] < len(a[0])]
    return neighbours

def getArea(i, j, a, visited):
    score = 0
    neighbours = getNeighbours(i, j, a)
    while(len(neighbours)):
         neighbour = neighbours[0]
         if neighbour[0]*len(a) + neighbour[1]  in visited:
            neighbours = neighbours[1:]
            continue

         if a[neighbour[0]][neighbour[1]] == 1:
            visited.add(neighbour[0]*len(a) + neighbour[1])
            score += 1
            neighbours = neighbours[1:] + getNeighbours(neighbour[0], neighbour[1], a)
         else:
            visited.add(neighbour[0]*len(a) + neighbour[1])
            neighbours = neighbours[1:]
    return score, visited
            
            
all_ones = []

for idx_i, row in enumerate(a):
    for idx_j, col in enumerate(row):
        if a[idx_i][idx_j] == 1:
           all_ones.append((idx_i, idx_j))

visited = set()
areas = []
for one in all_ones:
    if one[0]*len(a) + one[1] not in visited:
       area, visited = getArea(one[0], one[1], a, visited)
       areas.append(area)

    else:
       pass
print(max(areas))
