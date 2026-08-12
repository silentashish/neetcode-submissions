class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row = len(board)
        col = len(board[0])

        words_set = set(words)
        prefix_set = set()

        for word in words:
            for i in range(1, len(word)+1):
                prefix_set.add(word[:i])
        
        result = set()
        def dfs(i, j, cur_word):
            if i >= row or j >= col or i < 0 or j < 0:
                return
            
            if board[i][j] == '#':
                return

            word =  cur_word + board[i][j]
            if word not in prefix_set:
                return

            if word in words_set:
                result.add(word)
            
            original = board[i][j]

            board[i][j] = '#'

            dfs(i+1, j, word)
            dfs(i-1, j, word)
            dfs(i, j-1, word)
            dfs(i, j+1, word)

            board[i][j] = original
            
        for i in range(row):
            for j in range(col):
                dfs(i, j, '')
        
        return list(result)
        