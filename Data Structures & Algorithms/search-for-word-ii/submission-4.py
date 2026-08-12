class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row = len(board)
        col = len(board[0])

        words_set = set(words)

        root = TrieNode()

        for word in words:
            curr = root
            for i in word:
                if not i in curr.children:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
            curr.endOfWord = True
        
        result = set()
        def dfs(i, j, node, cur_word):
            if i >= row or j >= col or i < 0 or j < 0:
                return
            
            if board[i][j] == '#':
                return
            
            c = board[i][j]

            # Not a prefix of any word
            if c not in node.children:
                return

            node = node.children[c]
            word = cur_word + c

            if node.endOfWord:
                result.add(word)
            
            original = board[i][j]

            board[i][j] = '#'

            dfs(i+1, j, node, word)
            dfs(i-1, j, node, word)
            dfs(i, j-1, node, word)
            dfs(i, j+1, node, word)

            board[i][j] = original
            
        for i in range(row):
            for j in range(col):
                dfs(i, j, root, '')
        
        return list(result)
        