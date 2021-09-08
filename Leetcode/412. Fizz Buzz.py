def fizzBuzz(n):
    """
     Given an integer n, 
     return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i if non of the above conditions are true.

    """
    arr=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            arr.append("FizzBuzz")
        elif i%3==0:
            arr.append("Fizz")
        elif i%5==0:
            arr.append("Buzz")
        else:
            arr.append(str(i))
    
    return arr

n = 3
n = 5
n = 15
print(fizzBuzz(n))

         