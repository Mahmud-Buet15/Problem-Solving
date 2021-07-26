def strStr(haystack,needle):
    """
    Takes two strings as input. 
    Returns needle exists in haystack then returns index of the first occurance.
    If doesn't exists then returns -1. If needle is empty string ,returns 0

    """
    if len(needle)==0:
        return 0
    elif needle in haystack:
        x=haystack.index(needle)
        return x
    else:
        return -1
    
# haystack = "hello"
# needle = "ll"
# haystack = "aaaaa"
# needle = "bba"
haystack = ""
needle = ""

print(strStr(haystack,needle))
    

