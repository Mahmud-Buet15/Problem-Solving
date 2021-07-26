def titleToNumber(s):
    """
    Takes a string as a columnTitle that represents the column title as appear in an Excel sheet,
    returns its corresponding column number.
    """
    #making a dictionary of numbers and letters
    numbers=list(range(1,27))
    # print(numbers)
    letters=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # print(letters)
    d=dict(zip(letters,numbers))
    # print(d)
    
    #getting title to number
    sum=0
    for i in range(len(s)):
        sum=d[s[-i-1]]*26**i+sum
    return sum
    
s=""
s="A" 
s="Z" 
s="AA" 
s="AZ"
s="ZY" 
s="FXSHRXW"
print(titleToNumber(s))