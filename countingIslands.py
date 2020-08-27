"""
Given a 2D grid, count the number islands in the array. Land is represented as
a 1 that's connected in the NSEW direction.
"""

# O(width * height)
def dfs(island, row, col):
  # check conditions
  if row < 0 or col < 0 or row > len(island[0]) - 1 or col > len(island[0]) - 1:
    return
  if island[row][col] == 0:
    return 

  # process cell
  island[row][col] = 0

  # call DFS as needed
  dfs(island, row + 1, col)
  dfs(island, row - 1, col)
  dfs(island, row, col + 1)
  dfs(island, row, col - 1)


def solution(island):
  count = 0

  for row in range(len(island)):
    for col in range(len(island[0])):
      if island[row][col] == 1:
        count += 1
        dfs(island, row, col)

  return count

print(solution([[1,1,1],[1,0,0],[0,1,0]])) #2
print(solution([[1,0,0],[0,1,0],[0,0,1]])) #3
print(solution([[1,1,1],[1,0,1],[0,1,1]])) #1

