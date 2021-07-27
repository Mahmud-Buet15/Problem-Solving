# def reverseString(s):   # O(N) complexity
#         """
#         Takes a string and reverses it.
#         Do not return anything, modify s in-place instead.
#         """
#         l=len(s)

#         for i in range(l//2):
#                 s[i],s[l-i-1]=s[l-i-1],s[i]    #swapping letters
#         return s


def reverseString(s):   # O(N) complexity
        """
        Takes a string and reverses it.
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1

        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
            
            
            
            
s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
k=reverseString(s)
print(k)