# Introduction to Algorithms

```
Algorithms is a step by step guide to solve the problems.

```
# Prerequisite for Algo  

```
Designing knowledge
Domain knowledge
Any langauages
H/w and OS
Analyzing ability
```

***
1. Priori Analysis:
***
```
1. Analysis of Algorithm
2. Independent of Language
3. Hardware Independent
4. Time and space function consume by algo 

```
***
2. Posteriori Testing
***

```
1. Analysis of Program
2. Language Dependent 
3. Hardware dependent
4. Watch time and and memory consume in bytes

```

# Characteristics of Algorithm
```
1. It take the input like 0 or more
2. it has the atleast 1 I/O output 
3. It has the definitensess can't use the 'root -1'
4. It has the finiteness , means must terminate after some time 
5. It must have the effectiveness
```
 
<h1> How to Write the Algorithm</h1>

```
algorithm swap(a,b)
Begin
    temp <- a;
    a <- b;
    b <- temp;
end
```
<h1> How to Analyze the Algorithm</h1>
```
1. Time: it should be time efficient , and analyse it based on the time function  
2. Space: memory criteria that how much it memory will take 
3. Network Criteria : how much data transfer will be done over a network 
4. Power Consumptions
5. CPU registers
```

# Example: 
```
algorithm swap(a,b)
{
    temp <- a; --------1
    a <- b; -----------1
    b <- temp; --------1

# so time function  the f(n)= 3, constant value.

1. Time Analysis:  x=5*a+6*b ------ each statement take the 1 unit of time. and time is constant 

2. Space Analysis: her variables are: a, b and temp so, s(n)=3 , means order of 1 is constant = O(1), so space = O(1)
 s(n) = 3 word 

}

```

# Frequency Count Method 1.:

```
A = [8,2,4,1,5];
Algorithm sum(A, n)
{
    S = 0;                          ________________(1)
    for(i=o , i<n, i++):           __________________(n+1)
    {
        S = S+A[i];                 _________________(n)

    }
    return s;                      __________________(1)
}

***Time Complexity: ***

1. for S=0 it will run 1 time
# if n=5 than here i wil run for 1 time, and i<n  will be n+1 and , i++ will be n
like : i =0 , 1, 2, 3, 4, at 5 it wil stop and the condtion was checkd for n+1 = 6 times

2. so the loop executes for n +1 times

3. Inside the loop it executes of the n times

4. and the return fun for 1 time So, 
time fun = f(n) = 2n+3

> so order of 'n'(degree of the polynomial) is  : O(n)

***Space Complexity: ***
1. here Size of the A will be n so: A---------n (words)
                                    n---------1 
                                    s---------1
                                    i---------1
  so s(n) = n+3 , 
  so degree is O(n)                                 

```

# Method 2: 

*** Frequency count for the n*n metrics ***

```
Algorithm Add(A,B,n)
{
    for(i=0;i<n;i++) -------------------------(n+1)
    #whatever for this loop inside will execute for n time and 
    {
        for(j=0;j<n;j++)----------------------n(n+1)   
        {
            c[i,j]=A[i,j]+B[i,j]; ------------(n*n)
        }
    }  
}
```
```
______________________________________________________
#Time complexity:
#Time function of this program is:       f(n)= 2n^2n+1
# and time complexity will be:          O(n^2)

# Space Complxity:
A------------------------------------------ - n^2  (bcz they are matrices of n*2 , 2D)
B-------------------------------------------- n^2 
C-------------------------------------------- n^2
n, i , j ------------------------------------- 1 (3 scalable variables)
so,         time complexity =                         S(n) = 3n^2+3
and degree of the ploynomial or space complexity=     O(n^2)
_______________________________________________________
```
# Qusetion #: 
```
 ```
Algorithm Add(A,B,n)
{
    for(i=0;i<n;i++)                        -------------------------(n+1)
    #whatever for this loop inside will execute for n time and 
    {
        for(j=0;j<n;j++)                       ----------------------n((n+1))   
        {
            c[i,j]=0;                                -----------------(n*n)
            for(k=0,k<n,k++)                        ----------------- (n+1)(n*n)
            {
                c[i,j]=c[i,j]+A[i,k]*B[k,j] ---------------------------(n*n*n)
            }            
        }
    }  
}
}_
```
```
______________________________________________________________________________________
 #                               SO the time complexity is: 2n^3+3n^2+2n+1
                                so time complexity is :   O(n^3)
#  and Space complexity: A, B , C =   A---n^2
                                      B----> n^2
                                      c__-> n^2
 and for the moduke i, j , k =    1.
 and systejmcytl                                     
# So the space or time complexity v:3n^2+3





```                           









