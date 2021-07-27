def reverseVowels(s):  # O(N) complexity
    """
    Given a string s, reverse only all the vowels in the string and return it.
    """
    
    temp=""
    vows=""
    vowels="aeiou"
    
    for i in s:
        if i.lower() in vowels:   #extracting the vowels
            vows=i+vows
    
    c=0
    for i in s:
        if i.lower() in vowels:  # replacing the vowels
            temp+=vows[c]
            c+=1
        else:
            temp+=i
            
    return temp

s = "hello"
s = "leetcode"
print(reverseVowels(s))
            
            