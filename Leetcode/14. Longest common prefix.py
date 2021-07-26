def check(s,arr):
    """ It will take a string and an array. It will check if all the component of 
    array contains the string"""
    sum=0
    l=len(s)
    for i in range(len(arr)):
        if s in arr[i][:l]:
            pass
        else:
            sum+=1
    if sum>0:
        return False
    else:
        return True
    
# print(check("flo",["flower","flow","fluid"]))    
    
def longestCommonPrefix(arr):
    if len(arr)==1:
        return arr[0]
    s=arr[0]
    prefix=""
    for i in range(len(s)):
        a=s[:i+1]
        if check(a,arr[1:])==True:
            prefix=a
        else:
            break
    return prefix

# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs=["a"]
# strs=["flower","flower","flower","flower"]
strs=["c","acc","ccc"]
print(longestCommonPrefix(strs))