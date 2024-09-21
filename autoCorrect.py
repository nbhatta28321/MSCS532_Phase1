from trieNode import TrieNode
        
class AutoCorrect:
    def __init__(self):
        self.root = TrieNode() #create object from TrieNode
        
    def insert(self, word):
        cur = self.root #point the current object to root node

        for i in word:
            if i not in cur.child: #if not in Trie node, create a new node
                cur.child[i] = TrieNode()
            cur = cur.child[i]   # if it is, point it to the same root node
        cur.tail = True # add end of node marker
        
    def search(self, input):
        cur = self.root

        for i in input: # check chracters deom the root nodes 
            if i not in cur.child: #return empty if not found
                return []
            cur = cur.child[i] #point it to the child node that contains the character

        return self.collect_words(cur, input) 
    
    def collect_words(self, cur, input): #search for remaining words in dictionary
        sugg = []

        if cur.tail: #if its end of character, add the word to the suggestion
            sugg.append(input)
        for k,v in cur.child.items(): #loop though the character and add character until the end of word make is received
            sugg.extend(self.collect_words(v, input + k))

        return sugg
