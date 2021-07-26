# 1. Store index positions of alphabets of each string in different array
# 2. match the arrays for each alphabet

## method 1
# def isIsomorphic(s, t):    # O(N^2) complexity
#     """
#     Takes two strings s and t, returns boolean.

#     """
#     if len(s)!=len(t):
#         return False
    
#     else:
#         temp1,temp2=[],[]
#         for i in range(len(s)):
#             if s[i] not in temp1:
#                 test_str=s[i]
#                 lst1 = [i for i in range(len(s)) if s.startswith(test_str, i)]  #finding the indexes of each string
#                 temp1.append(s[i])
#                 #print(lst1)

#             if t[i] not in temp2:
#                 test_str=t[i]
#                 lst2 = [i for i in range(len(t)) if t.startswith(test_str, i)]
#                 temp2.append(t[i])
#                 #print(lst2)
                
#             if lst1!=lst2:   #matching the indexes of strings
#                 return False
    
#     return True
    

#method 2

def isIsomorphic(s,t):  # O(N) complexity
    
    mapping_s_t = {}
    mapping_t_s = {}
    
    for c1, c2 in zip(s, t):
        
        # Case 1: No mapping exists in either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        
        # Case 2: Either mapping doesn't exist in one of the dictionaries or Mapping exists and
        # it doesn't match in either of the dictionaries or both            
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
        print(mapping_s_t)
        print(mapping_t_s)
        
    return True









s = "egg"
t = "add"
# s = "foo"
# t = "bar"
s = "paper"
t = "title"
# s="aaa"
# t="fff"
# s="qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"
# t="',.pyfgcrl/=aoeuidhtns-\\;qjkxbmwvz"
# s="leet"
# t="code"
print(isIsomorphic(s, t))


