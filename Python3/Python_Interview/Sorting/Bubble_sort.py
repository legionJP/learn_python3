
num_list = [2,5,8,34,24,67,8,0,1]

def sort_num(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]           # numbers are swaping 
                nums[j] = nums[j+1]
                nums[j+1]= temp
                
sort_num(num_list)
print(num_list)