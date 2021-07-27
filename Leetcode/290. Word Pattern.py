# 1. Create two dictionaries to hold mapping between two strings.




def wordPattern(pattern, s):  # O(N) complexity
    """
    Given a pattern and a string s, find if s follows the same pattern.
    Return boolean.
    """
    s1=pattern
    s2=s.split()
    d1,d2={},{}
    
    if len(s1)!=len(s2):
        return False
    
    for c1,c2 in zip(s1,s2):
        if (c1 not in d1) and (c2 not in d2): # If mapping doesn't exist,create new mapping
            d1[c1]=c2
            d2[c2]=c1
            
            # print(d1)
            # print(d2)
        elif d1.get(c1)!=c2 or d2.get(c2)!=c1: # If mapping exists, check for match
            return False
        
    return True
        
        
        
    
        
pattern = "abba"
s = "dog cat cat dog"
pattern = "abba"
s = "dog cat cat fish"
pattern = "aaaa"
s = "dog cat cat dog"
pattern = "abba"
s = "dog dog dog dog"
print(wordPattern(pattern, s))