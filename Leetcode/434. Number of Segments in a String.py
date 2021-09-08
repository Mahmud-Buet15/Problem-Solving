def countSegments(s):
    """
    You are given a string s, return the number of segments in the string. 

    """
    import re
    s=s.strip()
    if len(s)==0:
        return 0
    arr=re.split("[\s]+",s)   #split by one or more than one whitespace
    #print(arr)
    return len(arr)
    


s = "Hello, my name is John"
#s = "Hello"
#s = "love live! mu'sic forever"
s = ""
s="                "
s=", , , ,        a, eaefa"
#s="#@#!%^&*()_+QWERTYUIawefaef"
print(countSegments(s))