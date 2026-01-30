class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = s.upper()
        result = result.replace("-", "")
        first = len(result) % k
        hyphens = int(floor(len(result)/k))
        print(first)
        print(hyphens)
        index  = 0
        iterator = 0
        final_result = ""
        if first:
            for i in range(first):
                final_result += result[iterator + i]
            iterator += first
            if iterator < len(result):
                final_result += "-"
        while iterator < len(result):
            for i in range(k):
                final_result += result[iterator + i]
            iterator += k
            if iterator < len(result):
                final_result += "-"
        return final_result
        
