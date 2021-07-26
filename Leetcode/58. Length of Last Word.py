def lengthOfLastWord(s):
    """
    Given a string s consists of some words separated by spaces,
    return the length of the last word in the string. If the last word does not exist, return 0

    """
    lst=s.rstrip().split(" ")  #removing whitespaces after last word
    # print(lst)
    last_word=lst[-1]
    
    return len(last_word)
    
    
    
    
    
    
# s = "Hello World"
# s = " "
s="a "
# s="b   a    "
print(lengthOfLastWord(s)) 