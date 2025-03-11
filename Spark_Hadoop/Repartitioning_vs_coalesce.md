# Repartioning and Coalesce

![alt text](image-45.png)

# situaation
    - when there is multiple executer and one executer gets the large chunck of datasets than other has
    to wait for the one and the most of the executers are idle for long time 
![alt text](image-46.png)

# skewness in data 
![alt text](image-47.png)

# Partitions  Vs Coalesce 
    - repartioning do the suffling of the data 
    - but coalsece do the merging 
    - partionitn 
![alt text](image-48.png)

![alt text](image-49.png)
![alt text](image-50.png)


![alt text](image-51.png)

![alt text](image-52.png)

# convert data into the rdd to get number of the partitions : 128 MB's 1 partitions

![alt text](image-53.png)

![alt text](image-54.png)

# repartion on based on column : 
![alt text](image-55.png)

##### will create the null partitions if less records are there 

# Coalesce
![alt text](image-56.png)
![alt text](image-57.png)

![alt text](image-58.png)