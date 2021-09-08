# 1. Count all letters from string
# 2. only one letter with odd number of occurance can be taken.
#     So, we will take the largest one.Then we can make all other odd numbers to
#     even by substracting 1 from all of them.
# 3. All even must be taken.
# 4. Add them together


from collections import Counter

#method 1
# def longestPalindrome(s):     # O(N) complexity
#     """
#     Given a string s which consists of lowercase or uppercase letters,
#     return the length of the longest palindrome that can be built with those letters.

#     Letters are case sensitive, for example, 
#     "Aa" is not considered a palindrome here.
#     """
#     if len(s)==0:
#         return 0
#     if len(s)==1:
#         return 1
    
#     d=dict(Counter(s))
#     #print(d)
#     lst=list(d.values())
#     #print(lst,sum(lst))
#     odd_lst,even_lst=[],[]
    
#     for i in lst:    
#         if i%2==0:
#             even_lst.append(i)
#         else:
#             odd_lst.append(i)
#     #print(odd_lst, max(odd_lst))
#     #print(even_lst,sum(even_lst))
    
    
    
#     if len(odd_lst)!=0:
#         max_odd=max(odd_lst)      
#         odd_lst.remove(max_odd) # IMPORTANT!!! modifying the list. Not returning anything
#         #print(odd_lst)
#         sum_odd=sum(odd_lst)-len(odd_lst)   # transforming every odd to even by substracting 1 from every odd
        
#         longest_palindrome=max_odd+sum_odd+sum(even_lst)
#     else:
#         longest_palindrome=sum(even_lst)
        
#     return longest_palindrome



#method 2
def longestPalindrome(s):
    d=dict(Counter(s))
    lst=list(d.values())
    ans=0
    for i in lst:
        
        if ans%2==0 and i%2==1:  # taling a odd number
            ans+=i
        elif ans%2!=0 and i%2==1: #making other odd number even by substracting 1. Then adding them
            ans+=i-1
        else:                   #adding all even numbers
            ans+=i
    
    return ans



s = "abccccdd"
#s = "a"
#s = "bb"
s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(longestPalindrome(s))