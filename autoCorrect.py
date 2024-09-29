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

        for i in input: # check chracters from the root nodes with imput word
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
    
    def bigram(self, word):
        return [word[i] + word[i+1] for i in range(len(word)-1)]
    
    def similarity_ratio(self, a, b): #based on 2 characters bigram, return max similarity
        groupA, groupB = self.bigram(a), self.bigram(b)

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
        
        required_sim_ratio = 0.32

        max_sim = 0.0

        sim_words = []

        collected_sim_words = self.collect_words(cur.child[word[0]], word[0])
        for w in collected_sim_words: ##campare the ratio with max similarity abd required sim_ratio

            temp_sim = self.similarity_ratio(word, w)

            if ( max_sim > required_sim_ratio and temp_sim > required_sim_ratio) or temp_sim > required_sim_ratio:
                # print(f"The sim ratio of {word} when w={w} is {temp_sim}")

                max_sim = temp_sim
                sim_words.append(w)

        return sim_words if max_sim > required_sim_ratio else []      

