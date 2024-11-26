#--------------------------------------------------------------------------------------------------------------#
#                                Selection  Sort  
#--------------------------------------------------------------------------------------------------------------#

# in selection find the min value from the start to end -- 
# so end of the iteration min = find value 
# than swap min value with the first value ,
# so comapre every value and swap at ones


def select_sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]< nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos]= temp

        print(nums)

nums = [87,45,5,22,32,456,12,34]
select_sort(nums)
print(nums)

