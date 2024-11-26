#--------------------------------------------------------------------------------------------------------------#
#                                Bubble Sort  
#--------------------------------------------------------------------------------------------------------------#

# iterate over throught the list and compare the two values than swap them if 1st is less than 2nd 
# Value 

# comparing and swap -- in every iteration 

num_list = [34,5,6,89,45,13,87,45]

def sort(nums):
    for i in range(len(nums)-1,0,-1):  # going 7 to 7 in reverse
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1] = temp

sort(num_list)
print(num_list) 
