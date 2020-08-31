# -*- coding: utf-8 -*-
import Levenshtein as lst
class SimiDic(dict):
    def __init__(self,threshold=0.9):
        dict.__init__(self)
        self.t=threshold

    def __getitem__(self, des):
        max=0
        k=None
        for _k in dict.keys(self):
            ratio=lst.ratio(des,_k)
            if ratio>max:
                max=ratio
                k=_k
        if max>self.t:
            return dict.__getitem__(self,k), max
        else:
            return None, max



'''
s=SimiDic(0.9)
s["yy"]=9
s["yauuufa"]=8
s["x"]=7
print (s["yauu ufa"])
'''






