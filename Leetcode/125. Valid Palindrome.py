# remove all whitespace and pucntuation.
# make all alphabets lower 
# Check first and last index for match.
import re
def isPalindrome(s):
    """
    This function will take a string as input and return boolean.
    """
    s=re.sub(r"[^a-zA-Z0-9]","",s)   # removing all white space and punctuation
    print(s)
    s=s.lower()
    l=len(s)//2
    for i in range(l):
        if s[i]!=s[-i-1]:
            return False
    return True

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s=""
# s="a"
s="ab_a"
s="0P"
print(isPalindrome(s))