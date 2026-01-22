class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index_w = 0
        index_a = 0
        while index_w < len(word) and index_a < len(abbr):
            if word[index_w] == abbr[index_a]:
                index_w += 1
                index_a += 1
            elif 97 <= ord(abbr[index_a]) <= 122:
                return False
            else:
                # find number
                if ord(abbr[index_a]) == 48:
                    return False
                else:
                    number = ''
                    while(index_a < len(abbr) and 48 <= ord(abbr[index_a]) <= 57):
                        number += abbr[index_a]
                        index_a += 1
                    print(number)
                    index_w += int(number)
        if index_w == len(word) and index_a == len(abbr):
            return True
        return False
        
