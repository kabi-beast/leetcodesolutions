class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        k -= 1
        i = 0
        s_list = list(s)
        while i<k:
            #swap positions i and k
            tmp = s_list[i]
            s_list[i] = s_list[k]
            s_list[k] = tmp
            i += 1
            k -= 1
        return "".join(s_list)
        
