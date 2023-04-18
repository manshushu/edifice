import collections


class Solution:
    def firstUniqChar(self,s:str)-> str:
        dic=collections.OrderdDict()
        for c in s:
            dic[c]=not c in dic
        for k,v in dic.items():
            if v: return k
        return ' '