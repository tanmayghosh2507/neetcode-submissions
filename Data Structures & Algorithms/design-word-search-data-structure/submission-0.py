class Node:
    def __init__(self, c):
        self.char = c
        self.next = {} # key: char, value: Node
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.trie = Node('')

    def addWord(self, word: str) -> None:
        trie = self.trie
        for w in word:
            if w not in trie.next:
                trie.next[w] = Node(w)
            trie = trie.next[w]
        trie.is_end = True


    def search(self, word: str) -> bool:
        return self.recursive_search(word, 0, self.trie)

    
    def recursive_search(self, word: str, index: int, trie: Node) -> bool:
        if index >= len(word):
            return trie.is_end
        
        w = word[index]
        if w == '.':
            found = False
            for _, t in trie.next.items():
                found = self.recursive_search(word, index+1, t)
                if found:
                    return True
            
            return found
        
        if w not in trie.next:
            return False
        
        return self.recursive_search(word, index + 1, trie.next[w])
