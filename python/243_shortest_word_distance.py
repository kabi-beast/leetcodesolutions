class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        found = ""
        foundIndex = 0
        distance = math.inf
        for i in range(len(wordsDict)):
            print(wordsDict[i])
            if wordsDict[i] == word1:
                print("found word 1")
                if found == word1 or found == "":
                    found = word1
                    foundIndex = i
                    continue
                else:
                    here = i - foundIndex
                    if here < distance:
                        distance = here
                    found = word1
                    foundIndex = i
            elif wordsDict[i] == word2:
                print("found word 2")
                if found == word2 or found == "":
                    found = word2
                    foundIndex = i
                    continue
                else:
                    here = i - foundIndex
                    if here < distance:
                        distance = here
                    found = word2
                    foundIndex = i
        return distance
        
