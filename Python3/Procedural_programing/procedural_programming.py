'''
Python allows for object orient , procedrual and function   programming  Models 
that is called "Paradigms" 

Proceedural Prrogramming : It is the step by step instructions , and first stepto oop

procedural + object orient +functional it is easier to to follow the all approaches.

Procedural programming  structures the code into the procedurres called the subtask. 

   ''' 

'''
Pricipal for the procedural programming is called the DRY :
    
   # Don't Repeate Yourself 
   for reducing the duplication code .

   procedure for getting the calculaitng the bill total prograam

   1). Total_bill function 

def bill_total_function(bill):
         total=0.00
         for k v in bill.itmes():   
         total += v
         return total
2) calculate_Tax_function:
    tax_total
def calculate_tax(percent, bill_total): 4. -- Calculate tax reuses the bill_total
       #accepts the 2 parameters 
      return round(percent*bil_total)/100.0 ,2) 3. -- bill reuses the food total
food_bill={'juice':3.5,1:3,3:4,4:5}
tax_total= calculate_tax(15, food-total) 2. -- Resuse the tax total 
print(food_total)            1 -- Food tatal is reuses and food bill
print(bill_total) and overall total 

'''

#Sometimes procedural programming is hard to maintain , It doesn't relate well and expose the data 

'''________________________________
 Algorithm:
________________________________

It is the series of the task to solve a problem pr task of a given problem

1.Simple 

2.Complex 
'''
# program to check the palnidrome word

def ispalindrom(str):
 
 startIndex = 0
 endindex = len(str)-1
 for i in str:
  if str[startIndex] != str[endindex]:
   return False
  else:
   return True
print(ispalindrom('racecar'))  

 

  
'''
# Python code to find vowel and consonant in string

def findVowel(string, vowel):
    
   # dictionary
   count = {}.fromkeys(vowel, 0)
   string = string.casefold()
    
   # vowel letters
   for ch in string:
      if ch in count:
        count[ch] += 1
   return count

def findConsonant(string, consonant):
    
   # using dictionary
   count = {}.fromkeys(consonant, 0)
   string = string.casefold()
    
   # consonants letters
   for ch in string:
      if ch in count:
        count[ch] += 1
   return count

# input from the user
string = input('String: ')

vowel = 'aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz '


# calling function
print(findVowel(string, vowel))
print(findConsonant(string, consonant))'''
