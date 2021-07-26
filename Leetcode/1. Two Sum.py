# def twoSum(nums, target):
#     """
#     Given an array of integers nums and an integer target, 
#     returns indices of the two numbers such that they add up to target.

#     """
#     for i in range(len(nums)):
#         a=nums[i]      #the first number. Index in i
#         b=target-a    #the second number . If exists in the list ,then find its index
        
#         if b in nums[i+1:]:   #exclude a
#             i_2=nums[i+1:].index(b)+i+1
#             return [i,i_2]



def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    returns indices of the two numbers such that they add up to target.

    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]+nums[j]==target:
                return [i,j]
         
nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6
print(twoSum(nums, target))