# To reverse the string provided by the user



def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = input("Enter The String You Want To Reverse : ")
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string(using loops) is : ", end="")
print(reverse(s))
