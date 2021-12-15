import copy
import math
import time

def printState(arr):
  print("")
  for row in arr:
    for col in row:
      print(col, end =" ")
    print("")
  print("")

def getIndexesOf(element, boardState):
  returnList = []
  for i in range(0, len(boardState)):
    for j in range(0, len(boardState[i])):
      if int(boardState[i][j]) == element:
        returnList.append(tuple([i, j]))
  return returnList

def cellIndex(r, c):
  return (math.floor(r/3), math.floor(c/3))

def fillableElements(r, c, arr):
  elementsInRow = [ele for i, ele in enumerate(arr[r]) if ele != 0]
  elementsInColumn = [arr[i][c] for i in range(0, len(arr)) if arr[i][c] != 0]
  cellI = cellIndex(r, c)
  lowerRow = cellI[0] * 3
  upperRow = (cellI[0] * 3) + 2
  lowerCol = cellI[1] * 3
  upperCol = (cellI[1] * 3) + 2
  elements = []
  for i in range(lowerRow, upperRow + 1):
    for j in range(lowerCol, upperCol + 1):
      if arr[i][j] != 0:
        elements.append(arr[i][j])
  toBeRemoved = elements + elementsInRow + elementsInColumn
  return list(set([i for i in range(1, 10)]) - set(toBeRemoved))

def fillNumbers(r, c, arr):
  global initState
  global zeros
  global parentState
  global loop
  global preFilledZeros
  fillEle = fillableElements(r, c, arr)
  copiedArr = copy.deepcopy(arr)
  for ele in fillEle:
    arr[r][c] = ele
    if str(arr) not in visitedStates:
      initState[r][c] = ele
      preFilledZeros.append([r, c])
      visitedStates.append(str(arr))
      break
  else:
    if len(preFilledZeros):
      lastInsert = preFilledZeros[-1]
      copiedArr[lastInsert[0]][lastInsert[1]] = 0
      initState = copy.deepcopy(copiedArr)
      preFilledZeros.pop()
    else:
      initState = parentState
      loop = False

def getMinRemValIndex(remArr):
  values = [len(fillableElements(arr[0], arr[1], initState)) for arr in remArr]
  return values.index(min(values))

smart = True if input("Use Smart Backtracking ?(y/n)").lower() == 'y' else False
startTime = time.time()
initState = []
visitedStates = []
preFilledZeros = []
with open('sudoku.txt') as f:
  lines = f.readlines()
  lines = [line.strip() for line in lines]
  for line in lines:
    initState.append([int(char) for char in line])
parentState = copy.deepcopy(initState)
printState(initState)
loop = True
count = 0
while loop:
  count += 1
  zeros = getIndexesOf(0, initState)
  if len(zeros):
    index = getMinRemValIndex(zeros) if smart else 0
    fillNumbers(zeros[index][0], zeros[index][1], initState)
  else:
    loop = False
print("Time taken for the solution - ", str(round(time.time() - startTime, 3)), " seconds")
print("Steps taken to arrive at the solution - ", count)
print("The solution is - ")
printState(initState)