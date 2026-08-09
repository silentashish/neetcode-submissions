class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.endOfWord

            c = word[index]

            if c != '.':
                if c not in node.children:
                    return False

                return dfs(index + 1, node.children[c])

            # c == '.'
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)