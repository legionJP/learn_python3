# Spark_Join_Suffle_sort

![alt text](image-59.png)

# Data Distribution

![alt text](image-60.png)

![alt text](image-61.png)

![alt text](image-62.png)

![alt text](image-63.png)

![alt text](image-64.png)

![alt text](image-65.png)

# Join Strategies in Spark 

![alt text](image-66.png)

![alt text](image-67.png)

# Suffle sort merge join 
    - olog(n)
    - utilize the cpu 
![alt text](image-68.png)


# Suffle Hash Join 
    - It will use the memory to do hashing 
    - 0(1)
    - if there is memory in executor then it will be suitable 

![alt text](image-69.png)

#
# Broadcast Hash Join 
    - decide the size of the broadcast data based on your  cluster size 
![alt text](image-70.png)

![alt text](image-71.png)

![alt text](image-72.png)


# example 
![alt text](image-73.png)

![alt text](image-74.png)
# sort_merge_plan to see the physical plan 

