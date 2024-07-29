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

# Frequency Count Method:

