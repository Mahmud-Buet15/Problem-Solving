def convertToTitle(columnNumber):
    """
    This function takes an integer columnNumber and
    returns its corresponding column title as it appears in an Excel sheet.

    """
    # #making a dictionary of numbers and letters
    # numbers=list(range(1,27))
    # # print(numbers)
    # letters=[i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # # print(letters)
    # d=dict(zip(numbers,letters))
    # # print(d)
    
    lst = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    
    #getting column title
    result=columnNumber
    title=""

    while True:
        if result==0:
            break
        
        if result<26:
            title=lst[result]+title
            break
        else:
            mod=result%26
            result=result//26
            if mod==0:       #we have to be careful for this case
                title=lst[mod]+title
                result=result-1
            else:
                title=lst[mod]+title
            
            if result==0:
                break
        
    return title
    
    

columnNumber=0
columnNumber=1
# columnNumber=26
# columnNumber=52
# columnNumber=78
# columnNumber=28
# columnNumber = 701 
# columnNumber = 2147483647  
print(convertToTitle(columnNumber))