class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word != "":
            self.d[len(word)].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for w in self.d[len(word)]:
            for i in range(len(w)):
                if w[i] != word[i] and word[i] != ".":
                    break
            else:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
