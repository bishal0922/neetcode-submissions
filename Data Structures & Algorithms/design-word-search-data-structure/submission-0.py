class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    
    def search(self, word: str) -> bool:
        
        def dfs(i, curr):
            # Base case: if we've gone through the whole word, 
            # return True ONLY if this node marks the end of a real word.
            if i == len(word):
                return curr.isEnd
            
            c = word[i]
            
            if c == '.':
                # Wildcard: try ALL children of the current node
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            
            else:
                # Regular letter: check if it exists in current node's children
                if c not in curr.children:
                    return False
                # Move deeper down the Trie to the child node
                return dfs(i + 1, curr.children[c])

        # Kick off the search starting at index 0 and the root node
        return dfs(0, self.root)