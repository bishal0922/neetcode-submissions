class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.end = True 

    def lcp(self) -> str:
        node = self.root
        prefix = []


        while len(node.children) == 1 and not node.end:
            print(list(node.children.keys()))
            char = list(node.children.keys())[0]
            prefix.append(char)

            node = node.children[char]

        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if "" in strs: return ""

        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.lcp()

