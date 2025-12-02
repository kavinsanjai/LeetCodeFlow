class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows=len(board)
        cols=len(board[0])
        dirs=((1,0),(0,1),(-1,0),(0,-1))
        visited=set()


        def dfs(i,j):
            board[i][j]='S'
            visited.add((i,j))
            for di,dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0<= nj < cols and board[ni][nj] == 'O' and (ni,nj) not in visited:
                    dfs(ni,nj)

        
        for i in range(rows):
                if board[i][0]=='O' and (i,0) not in visited:
                    dfs(i,0)
                if board[i][cols-1]=='O' and (i,cols-1) not in visited:
                    dfs(i,cols-1)

        for j in range(cols):
            if board[0][j]=='O' :
                dfs(0,j)
            if board[rows-1][j]=='O':
                dfs(rows-1,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'
    



        
        