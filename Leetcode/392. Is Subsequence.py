
# a="mahmud"
# b=iter(a)
# "m" in b  #true
# "m" in b  #true
# "m" in b #false

# Using iterator we can cut 't' after finding a character!!!! 
# The beauty is that iterator is only used once in Python.After using iterator, you cannot use it anymore

def isSubsequence(s, t):
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.


    """
    
    remainder_of_t = iter(t)
    for letter in s:
        if letter not in remainder_of_t:  #after comparison the letter is cut off from remainder_of_t
            return False
    return True
    

s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
# s="ab"
# t="baab"
# s=""
# t="ahbgdc"

# s="b"
# t="c"
# s="abc"
# t=""

# s="bb"
# t="ahbgdc"
print(isSubsequence(s, t))