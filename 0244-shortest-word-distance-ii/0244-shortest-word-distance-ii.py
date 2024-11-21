class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.indices = defaultdict(list)
        
        for i, v in enumerate(self.wordsDict):
            self.indices[v].append(i)

        

    def shortest(self, word1: str, word2: str) -> int:

        res = float("inf")
        
        word1Indexes = self.indices[word1]
        word2Indexes = self.indices[word2]

        i, j = 0, 0

        while i < len(word1Indexes) and j < len(word2Indexes):
            res = min(res, abs(word1Indexes[i] - word2Indexes[j]))

            if word1Indexes[i] < word2Indexes[j]:
                i += 1
            
            else:
                j += 1

        
            
        return res if res > 0 else None
            

        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)