#1. Using the brute force
# Complexity : s+t= o(nlogn+mlogm)
def isAnagram(s:str, t:str)-> bool:
        """
        :type s: str    
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
             return False
        return sorted(s.lower())==sorted(t.lower())
          
s= "racecar"
t="areccar"
print(isAnagram(s,t))

# 2. Using the char frequency count by hash map
def isAnagramHash(s,t):
    s,t= s.lower(),t.lower()
    CountS, CountT ={},{}
    if len(s)!=len(t):
            return False
    # Building the Has Table 
    for i in range(len(s)):
            CountS[s[i]]= 1+CountS.get(s[i],0) # increase count by 1 if the value key
            CountT[t[i]] = 1+CountT.get(t[i],0)
#    for c in CountS:
#           if CountS[c]!=CountT.get(c,0):
#                  return False
#   return True
    return CountS==CountT

          
s= "racecar"
t="Rraacce"
print(isAnagramHash(s,t))


### 3. using the ord fun and the list for 26 

def isAnagramOrd(s,t):
        count =[0]*26
        if len(s)!=len(t):
              return False
        for i in range(len(s)):
              count[ord(s[i].lower())-ord('a')] +=1
              count[ord(t[i].lower())-ord('a')] -=1
        for val in count:
               if val!=0:
                      return False
        return True

          
s= "racecar"
t="Rraacce"
print(isAnagramOrd(s,t))