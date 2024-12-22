def selection_sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j]< nums[minpos]:
                minpos = j
            temp = nums[i]
            nums[i]= nums[minpos]
            nums[minpos] = temp

sort_list = [2,34354,6,67,8,9,0,1]
selection_sort(sort_list)
print(sort_list)          