# '''
# In the enchanted forest of Snoopville, the wise owl known as Orlon is the guardian of the mystical treasure. Every year, Orlon holds a challenge to find the worthy adventurer who can solve the riddles of the forest and earn the treasure.

# The challenge is simple but requires both wit and knowledge of the forest’s magical rules. The adventurer must speak a word aloud within 5 seconds after the bell rings. However, only those who meet the conditions of the forest will qualify for the treasure hunt.

# To qualify for the next round of the challenge, the word spoken by the adventurer must:

# Contain at least 2 vowels.
# The number of consonants in the word must be a perfect square of a prime number (from the sequence: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2, 17^2, 19^2,.......).
# if the word has no consonants, the adventurer will be disqualified.
# As the judge of the challenge, your task is to determine whether each adventurer qualifies for the next stage based on their word.

# Input Format
# The only line of input contain a single word consisting of uppercase or lowercase alphabets.

# Output Format
# Print "Qualify" if the adventurer qualifies, otherwise print "Disqualify".

# Constraints
# 1 <= |word| <= 10^5

# Sample Testcase 1
# Testcase Input
# Challenge
# Testcase Output
# Disqualify
# Explanation
# Vowel(s): A,, E, E (3 vowels)
# Consonants: C, H, L, L, N, G (6 consonants)
# 6 consonants does not meet the required condition (6 is not a perfect square of a prime number).
# Sample Testcase 2
# Testcase Input
# BeUnstoppables
# Testcase Output
# Qualify
# Explanation
# Vowel(s): E, U, O, A, E (5 vowels)
# Consonants: B, N, S, T, P, P, B, L, S (9 consonants)
# 9 consonants : 9 is the perfect square of 3.
# '''

# import math 
# def is_prime(number):
#   if number<1:
#     return false
#   for i in range(2, int(number**0.5)+1):
#     if number%i ==0:
#       return False
#   return True

# def is_square_prime(number):
#   sqrt = int(math.sqrt(number))
#   if sqrt*sqrt == number and is_prime(sqrt):
#     return True
#   return False

# int_str = str(input()).lower()

# vowel = "aeiou"
# consonants = "bcdfghjklmnpqrstvwxyz"
# count_v = 0
# count_c =0
# for x in int_str:
#   if x in vowel:
#     count_v+=1
#   if x in consonants:
#     count_c+=1
# if count_c>=2 and is_square_prime(count_c):
#   print("Qualify")
# else:
#   print("Disqualify")

# # Question 2:
# '''
# Problem Statement
# You are given two arrays, A and B. The array A is of length N and contains N positive integers. The array B is initially empty. At the start, you can take any element from array A and put it in array B. After this initial step, you can take any element from array A and any element from array B. Add the GCD value of these two integers to your score and insert both elements into array B. When you take any element from A, it is automatically deleted from array A. Determine the maximum score you can achieve if you play optimally.

# Input Format
#  The first line of input will be one integer “N” denoting the length of the array A.

# The next line of input contains “N” space separated integers denoting the array elements.

# Output Format
# print an integer denoting the maximum score you can achieve.

# Constraints
# 1<= N <= 10^3

# 1<= A[i]<=10^3

# Sample Testcase 1
# Testcase Input
# 5
# 2 4 3 6 1
# Testcase Output
# 8
# Explanation
# We can first take 6 in the array B. Then take 3 so the score will be GCD(6,3) =3.

# Then add 2 and the score will be 3 + GCD(6,2) = 5.

# Then add 4, the score will be 5 + GCD(2,4) = 7.

# And at the last add 1 so the final score will be 7 + GCD(2,1) =8.

# Sample Testcase 2
# Testcase Input
# 4
# 1 2 3 4
# Testcase Output
# 4
# Explanation
# First take 4 in array B then 2, 3 and 1. When we are inserting 2 the score will  be GCD(4,2) =2,

# Then 2+ GCD(2,3) + GCD (2,1) = 4.
# '''

# import math
# from collections import defaultdict

# # Function to find GCD
# def findGCD(n1, n2):
#     return math.gcd(n1, n2)

# # Function to determine the maximum score
# def max_score(A):
#     N = len(A)
#     B = []
#     score = 0

#     # Sort array A in descending order to maximize the GCD value addition
#     A.sort(reverse=True)

#     # Initial step: take the largest element from A and put it in B
#     B.append(A.pop(0))

#     while A:
#         best_gcd = -1
#         best_index = -1

#         # Find the best pair (a, b) which gives the maximum GCD
#         for i in range(len(A)):
#             for b in B:
#                 gcd_value = findGCD(A[i], b)
#                 if gcd_value > best_gcd:
#                     best_gcd = gcd_value
#                     best_index = i

#         # Add the best pair's GCD to the score and move the element to B
#         score += best_gcd
#         B.append(A.pop(best_index))

#     return score

# # Input
# N = int(input())
# A = list(map(int, input().split()))

# # Calculate the maximum score
# result = max_score(A)

# # Output the result
# print(result)


# #  Question 3
# '''
# Raj invented a new type of fibonacci series where each element is a binary string ( binary string is a string which contains only “0” and “1” s). In this series F(1) = “0” , F(2) = “1” F(3) = “01” ………..  F(n) = F(n-2) + F(n-1). Puja finds this series interesting and wants to judge whether Raj invented the series on his own or not. So puja will aske q queries and in each query he will give a positive integer n . Raj needs to tell the absolute difference of the number of “0's" and “1's" in F(n). Help Raj to answer all the queries.

# Write a program to determine the  absolute difference of the number of “0's" and “1's" in F(n) for each query.

# As the number can be very large print the answer modulo 1e9+7.

# Input Format
#  The first line of input will be one integer Q denoting the number of queries.

# The next Q line of input will contain a positive integer n.

# Output Format
# For each query print  the absolute difference of the number of “0's" and “1's" in F(n).

# As the number can be very large print the answer modulo 1e9+7.

# Constraints
# 1<= Q <= 10^6

# 1<= n <= 10^7

# Sample Testcase 1
# Testcase Input
# 3
# 4
# 5
# 6
# Testcase Output
# 1
# 1
# 2
# Explanation
# F(4) = “101” so the absolute difference between the number of “1’s” and the number of “0’s” is 1.

# F(5)= “01101” and F(6) = “10101101” so the  absolute difference between the number of “1’s” and the number of “0’s” are 1 and 2 respectively.

# Sample Testcase 2
# Testcase Input
# 2
# 7
# 3
# Testcase Output
# 3
# 0
# Explanation
# F(7) = “0110110101101” , here the number of “1’s” is 8 and number of “0’s” is 5 so the absolute difference is 3.

# F(3) = “01” so the absolute difference is 0.
# '''

MOD = int(1e9 + 7)

def compute_fibonacci_diff(max_n):
    dp = [0] * (max_n + 1)
    count_zeros = [0] * (max_n + 1)
    count_ones = [0] * (max_n + 1)
    
    if max_n >= 1:
        count_zeros[1] = 1
        count_ones[1] = 0
    if max_n >= 2:
        count_zeros[2] = 0
        count_ones[2] = 1
    
    for i in range(3, max_n + 1):
        count_zeros[i] = (count_zeros[i-2] + count_zeros[i-1]) % MOD
        count_ones[i] = (count_ones[i-2] + count_ones[i-1]) % MOD
        dp[i] = abs(count_zeros[i] - count_ones[i]) % MOD
    
    return dp

# Input
Q = int(input())
queries = [int(input()) for _ in range(Q)]

# Precompute the differences for the maximum query value
max_n = max(queries)
diffs = compute_fibonacci_diff(max_n)

# Output the results for each query
for n in queries:
    print(diffs[n])
