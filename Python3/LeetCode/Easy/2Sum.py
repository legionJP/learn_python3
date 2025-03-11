# 2 Sum 
# solution 1: 
#1.  Brute Force 
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                        if nums[i]+nums[j] ==target:
                                return [i,j]
        return []

from typing import List

#2.  Hash Map 
def twoSumHash(nums: List[int], target: int)-> List[int]:
        prevHash= {} # val: index

        for i , n in enumerate(nums):
                complement = target-n
                if complement in prevHash:
                        return [prevHash[complement],i]
                prevHash[n]=i
        return 
#3. 

# Solution Approach
nums =[3,2,4]
target =6
print(twoSum(nums,target))
print(twoSumHash(nums,target))



## Solution approach

#def twoSum(nums, target):

   # first, end = 0, 1
        # # while first<end:
        # for _ in range(len(nums)):
        #     current_sum = nums[first]+nums[end]
        #     if current_sum == target:
        #         return [first,end]
        #     elif current_sum < target:
        #         first +=1
        #         end+=1
        #     # else:
        #     #     end-=1
        # # return None

def isAnagram(s, t):
        """
        :type s: str    
        :type t: str
        :rtype: bool
        """
        if sorted(s.lower())==sorted(t.lower()):
            return True
        else:
            return False

s= "racecar"
t="arcecar"
print(isAnagram(s,t))