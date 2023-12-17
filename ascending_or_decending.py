 # so there is gonna be a sequence of numbers and we are gonna tell if they are ascnding or decending 
 # this file is used for lines_of_code.py

n = 0 
while n <= 0 :
  n = int(input("enter how many numbers we are going to use: "))
message = "So we are going to use {} numbers"
print(message.format(n))

num1 = int(input("Enter: "))

dec = False
inc = False
both = True
i = 0 

while i < n-1 :
  num2 = int(input("Enter: "))
  diff = (num2 - num1)

  if diff < 0 :
    dec = True
    both = False
  if diff > 0 :
    inc = True
    both = False
  num1 = num2 
  i += 1    

if both :
  print("It could be incremental or decremental")
elif inc and dec :
  print("Neither incremental or decremental ")
elif inc :
  print("Its incremental")
else: 
  print("Its decremental")      




