from typing import List
## Brtue Forec: 
## time- O(n^2)
## space- O(1)

def hasDuplicate(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Using the Sort 
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1,len(nums)):
                if nums[i] == nums[i-1]:
                    return True
        return False


# Using the Hash Set
# time and Space- (O(n) 
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        # Or using the Hash Set length
        #return len(set(nums)) < len(nums)


