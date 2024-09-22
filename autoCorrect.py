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
                return self.correction(input) #if the word is incorrect
                # return []
            cur = cur.child[i] #point it to the child node that contains the character

        return self.collect_words(cur, input) 
    
    def collect_words(self, cur, input): #search for remaining words in dictionary
        sugg = []

        if cur.tail: #if its end of character, add the word to the suggestion
            sugg.append(input)
        for k,v in cur.child.items(): #loop though the character and add character until the end of word make is received
            sugg.extend(self.collect_words(v, input + k))

        return sugg
    
    def biagam(self, word):
        return [word[i] + word[i+1] for i in range(len(word)-1)]
    
    def similarity_ratio(self, a, b):
        groupA, groupB = self.biagam(a), self.biagam(b)

        similarity = []

        for i in range(len(groupA)):

            try:
                groupB.index(groupA[i])
                similarity.append(groupA[i])
            except:
                continue

        return len(similarity)/max(len(groupA), len(groupB))   
    
    def correction(self, word):

        cur = self.root
        
        required_sim_ratio = 0.3

        max_sim = 0.0

        sim_words = []

        collected_sim_words = self.collect_words(cur.child[word[0]], word[0])
        for w in collected_sim_words:

            temp_sim = self.similarity_ratio(word, w)

            if temp_sim > max_sim or temp_sim > required_sim_ratio:
                # print(f"The sim ratio of {word} when w={w} is {temp_sim}")

                max_sim = temp_sim
                sim_words.append(w)

        return sim_words if max_sim > required_sim_ratio else word      

