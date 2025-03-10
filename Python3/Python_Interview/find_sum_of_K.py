# add two element from the list to check if the sum equals to a variable k

def find_pair_sum(nums, target):

    # # 1. Using the Hash Map 
    # seen= {}
    # for num in nums:
    #     complement = target-num
    #     if complement in seen:
    #         return complement , num
    #     else:
    #      seen[num] = True
    # return None

# Logic ==> the complement will be the k-num where it will be c= 15-num = num+c == K, so when each complement is stroed in hastable
# dict of seen and searching if the complement c = num in the nums list , means the complement of new num is  found in seen then its result

# 2. Using the Two Pointer
    nums.sort()
    l , r = 0 ,len(nums)-1
    while l<r:
        current_sum = nums[l]+ nums[r]
        if current_sum == k:
            return nums[l], nums[r], [l,r]
        
        elif current_sum < k:
            l += 1
        else:
            r -= 1
    return None
        
# Example usage
nums = [3,2,4]
k = 6
result = find_pair_sum(nums, k)
print(result)  # Output: (7, 8)

# first assign the l and r 0 and array -1 to traverse
# than compare if the 