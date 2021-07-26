#O(n) time  O(1)space
#The way this works, is thanks to the stack(list) property of Fist in last out.

#If a opening bracket is found we push to the stack.

#If a closing bracket is found and stack is empty we return false since it never was opened.

#If a closing bracket is found we compare it to the last element in the stack using the matchingBrackets object
	#If it is true, we pop it out the stack, otherwise return false since they dont match.
	
#When finished iterating, we check if the stack is empty. If it is not then, return false since some brackets might have not found their pair. 

#if stack is empty all pairs of brackets have been matched and return true;

def isValid(s):
    """
    Takes a string as input and return boolean.
    """
    lst=[]
    open_bracket="({["
    close_bracket=")}]"
    matching_bracket={")":"(","}":"{","]":"["}
    
    for i in s:
        if i in open_bracket:
            lst.append(i)
        elif i in close_bracket:
            if len(lst)==0:
                return False
            elif matching_bracket[i]==lst[-1]:
                lst.pop()
            else:
                return False
    return len(lst)==0

# s = "()"
s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "{[]}"
# s="(])"
print(isValid(s))