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
