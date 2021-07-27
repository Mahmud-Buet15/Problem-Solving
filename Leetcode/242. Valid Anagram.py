# 1. Use two dictionaries to count occurance of each letters
# 2. match the number of occurances for each letter


# def isAnagram(s, t):   #O(N) complexity
#     """
#     Takes two strings, returns boolean.
#     """
#     if len(s)!=len(t):
#         return False
    
#     d1,d2={},{}
#     temp=set()
    
#     for c1,c2 in zip(s,t):
#         if c1 not in d1:
#             d1[c1]=s.count(c1)
#         if c2 not in d2:
#             d2[c2]=t.count(c2)
        
#         temp.add(c1)
#     # print(temp)
#     # print(d1)
#     # print(d2)
    
#     for i in temp:
#         if d1.get(i)!=d2.get(i):    # d1[i] will raise error if a doesn't exist 
#             return False
    
#     return True


# 2nd method
def isAnagram(s, t):   #O(N) complexity
    """
    Takes two strings, returns boolean.
    """
    from collections import Counter
    if len(s)!=len(t):
        return False
    
    d1=Counter(s)
    d2=Counter(t)
    
    for i in d1.keys():
        if d1.get(i)!=d2.get(i):    # d1[i] will raise error if a doesn't exist 
            return False
    
    return True
       
    

s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
# s="mah.m"
# t="mm.ha"
# s="a"
# t="ab"

print(isAnagram(s, t))