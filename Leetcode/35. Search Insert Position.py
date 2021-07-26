# def searchInsert(nums,target):
#     """
#     Given a sorted array of distinct integers and a target value,
#     returns the index if the target is found.
#     If not, return the index where it would be if it were inserted in order
#     """
#     if target==0:
#         return 0
#     if len(nums)==1:
#         if target>nums[0]:
#             return 1
#         else:
#             return 0
#     else:
#         pos=0
#         k=len(nums)//2
#         left=nums[:k]
#         right=nums[k:]
#         if target<=left[-1]:  #if the target is less than the max value of the list
#             pos=pos+searchInsert(left, target)
#         else:
#             pos=pos+len(left)+searchInsert(right, target)

            
#     return pos


#another method
def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = right - left // 2
            
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return left

nums = [1,3,5,6]
target = 5
nums = [1,3,5,6] 
target = 2
nums = [1,3,5,6]
target = 7
# nums = [1,3,5,6]
# target = 0
# nums = [1]
# target = 0
# nums = [1]
# target = 2
print(searchInsert(nums, target))