class TrieNode:
    def __init__(self):
        self.children = {}  # can store 'अ', 'आ', 'ा', 'ँ', 'ः' etc.
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:  # Devanagari chars are allowed
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def suggest(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        self._dfs(node, prefix, result)
        return result

    def _dfs(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)

        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, result)
