from collections import Counter
# c = Counter() 
# c = dict(Counter('gallahad') )
# print(c)
# d=list(Counter('gallahad') )
# print(d)

# 1. Count all letters from both strings
# 2. Check if all letters of ransomNote are available in magazine

def canConstruct(ransomNote, magazine):
    """
    Given two stings ransomNote and magazine, 
    return true if ransomNote can be constructed from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    """
    ran_dict=dict(Counter(ransomNote))
    ran_lst=list(ran_dict)
    mag_dict=dict(Counter(magazine))
    
    for i in ran_lst:
        if mag_dict.get(i)==None:
            return False
        if ran_dict.get(i)>mag_dict.get(i):
            return False
    
    return True
    
ransomNote = "a"
magazine = "b"
ransomNote = "aa"
magazine = "ab"
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
