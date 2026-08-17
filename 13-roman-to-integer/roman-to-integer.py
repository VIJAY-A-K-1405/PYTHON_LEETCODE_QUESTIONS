class Solution:
    def romanToInt(self, s: str) -> int:
        v = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        summ = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n-1 and v[s[i]] < v[s[i+1]]:
                summ += v[s[i+1]] - v[s[i]]
                i +=2
            else: 
                summ += v[s[i]]
                i+=1
        return summ
        
        
        
        # summ = 0
        # n = len(s)
        # for i in range(n):
        #     k = v[s[i]]
        #     if i + 1 < n and k < v[s[i+1]]:
        #         summ -= k
        #     else:
        #         summ += k
        # return summ

