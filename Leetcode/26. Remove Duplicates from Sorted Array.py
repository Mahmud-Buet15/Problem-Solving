def removeDuplicates(nums):
    """
    Takes a list and returns removing the duplicates

    """
    lst=[]
    for i in nums:
        if i not in lst:
            lst.append(i)
    k=len(lst)
    less=len(nums)-k
    for i in range(less):
        lst.append("_")
    return lst

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

