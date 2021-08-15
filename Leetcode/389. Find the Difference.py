# 1. Count letters from both strings
# 2. Compare the occurances:
#    a) If count(letter) is 1 in t and None on s. then return the letter 
#    b) elif count(letter) in greater in t than s. then return the letter


from collections import Counter
def findTheDifference(s, t):  # O(N) complexity. But a bit faster as we've used set here instead of list for traversing.
    """
    You are given two strings s and t.

    String t is generated by random shuffling string s and 
    then add one more letter at a random position.

    Return the letter that was added to t.



    """
    #counting the letters from both strings
    s_dict=dict(Counter(s))
    t_dict=dict(Counter(t))
    t_set=set(t_dict)   #we will traverse through this set
    
    for i in t_set:
        if t_dict.get(i)==1 and s_dict.get(i)==None:
            return i
        elif t_dict.get(i)>s_dict.get(i):
            return i
    
    

s = "abcd"
t = "abcde"
s = ""
t = "y"
s = "ae"
t = "aea"
print(findTheDifference(s, t))