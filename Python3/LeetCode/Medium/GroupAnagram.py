from ast import Str
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s) # if there is item of sorted str append
            else:
                anagrams[sorted_s] = [s] # if not asssign it 
        return list(anagrams.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         for group in anagrams.values():
#             result.append(group)
#         return result


from typing import List

# time complexity - m.nlogn
# Using the Default Dict :

def groupAnagrams(strs: List[str])-> List[List[str]]:
    result = defaultdict(list())
    for s in str:
        sorted_s = ''.join(sorted(s))
        result[sorted_s].append(s)
    return list(result.values())

# Using the list of the charcters 
# count_list =[0]*26
# 1e,1a,1t ---> Hasmap --> key 
# value: [anagram_list]
# key : [eat, tea]
# time complexity --> O(m*n*26)

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in res:
        count = [0]*26
        for c in s:
            count[(ord(c)-ord("a"))] +=1
        res[tuple(count)].append(s)
    return res.values()