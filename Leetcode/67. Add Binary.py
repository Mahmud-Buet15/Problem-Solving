
def addBinary(a, b):
    """
      Given two binary strings a and b, return their sum as a binary string.
    """
    bin_str="0b"
    a=int(bin_str+a,2) #converting binary to integer. Integer works with string format of binary number
    b=int(bin_str+b,2)
    result_bin=bin(a+b) #integer to binary
    result_str=str(result_bin)[2:]  #excluding "0b"
    return result_str

a = "11"
b = "1"
# a = "1010"
# b = "1011"
print(addBinary(a, b))