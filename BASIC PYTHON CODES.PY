# BASIC PROGRAM TO PRINT HELLO WORLD

print("hello world")
# OUTPUT -> hello world

# CHECK IF A NUMBER IS POSITIVE OR NEGATIVE OR ZERO

a = int(input("Enter the number you want to check : "))
if a>0:
    print("Positive")
if a<0:
    print("negative")
if a==0:
    print("Zero")
    
# PRINT SUM OF ALL EVEN NUMBERS TILL N

i=2
sum=0
n = int(input("Enter the number you want to check : "))
while i<=n:
    sum=sum+i
    i=i+2
print(sum)

# PRINT NUMBERS TILL 10

i=0
while i<11:
    print(i)
    i=i+1

    
#Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
#you need to convert all Fahrenheit values from Start to End at the gap of W,
#into their corresponding Celsius values and print the table.

S = int(input())
E = int(input())
W = int(input())
for i in range(S,E+1,W):
    C = ((S-32)*5)/9
    print(S," ",int(C))
    S=S+W
   

# How to check if a number is even number or odd number

n = int(input("Enter the number"))
if n/2==0:
    print("Even number")
else:
    print("Odd number")

    
# Check whether you are eligible to vote or not

age = int(input("Enter your age : "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
