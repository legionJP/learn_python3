# # if n%2 !=0
# # count+=1
# # return count
# # steps : find the nth term of prime number and then find the square of that number
# # 1. find the nth term of prime number
# # 2. find the square of that number
# # 3. return the square of that number
# # 4. Done

def nth_prime_square(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1  # This only runs if the loop completes without a break
    return num**2
print(nth_prime_square(3))  # Output: 25 (5^2)


