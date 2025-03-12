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

from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         anagrams = {}
#         for s in strs:
#             sorted_s = ''.join(sorted(s))
#             if sorted_s in anagrams:
#                 anagrams[sorted_s].append(s)
#             else:
#                 anagrams[sorted_s] = [s]
#         for group in anagrams.values():
#             result.append(group)
#         return result
        
