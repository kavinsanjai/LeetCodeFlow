class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
            totalRows = len(grid)
            totalCols = len(grid[0])

            rowPrefix = [[0] * (totalCols + 1) for _ in range(totalRows)]
            colPrefix = [[0] * totalCols for _ in range(totalRows + 1)]

            for r in range(totalRows):
                for c in range(totalCols):
                    rowPrefix[r][c + 1] = rowPrefix[r][c] + grid[r][c]
                    colPrefix[r + 1][c] = colPrefix[r][c] + grid[r][c]

            maxPossibleSide = min(totalRows, totalCols)

            for sideLength in range(maxPossibleSide, 1, -1):
                for r in range(totalRows - sideLength + 1):
                    for c in range(totalCols - sideLength + 1):
                        primaryDiagSum = 0
                        secondaryDiagSum = 0

                        for k in range(sideLength):
                            primaryDiagSum += grid[r + k][c + k]
                            secondaryDiagSum += grid[r + k][c + sideLength - 1 - k]

                        if primaryDiagSum != secondaryDiagSum:
                            continue

                        targetSum = primaryDiagSum
                        isValid = True

                        for k in range(sideLength):
                            currentRowSum = (
                                rowPrefix[r + k][c + sideLength] - rowPrefix[r + k][c]
                            )
                            currentColSum = (
                                colPrefix[r + sideLength][c + k] - colPrefix[r][c + k]
                            )

                            if currentRowSum != targetSum or currentColSum != targetSum:
                                isValid = False
                                break

                        if isValid:
                            return sideLength

            return 1