# a="mahmud"
# for i,letter in enumerate(a):
#     print(i,letter)


# 1. Count all letters from string
# 2. Use a loop to check which has 1 occurance

from collections import Counter

def firstUniqChar(s):  # O(N) complexity
    """
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1.

    """
    d=dict(Counter(s))
    temp=set()
    
    for index,letter in enumerate(s):
        if letter in temp:
            continue
        elif d.get(letter)==1:
            return index
        temp.add(letter)
    
    return -1

s = "leetcode"
s = "loveleetcode"
s = "aabb"
print(firstUniqChar(s))
        