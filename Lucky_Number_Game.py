import random


for i in range(20):
    a = int(input("Enter Your Number :"))
    b = random.randint(1,20)
    if(a == b):
       print("You Win")
       print("The output value is",b)
       break
    else:
       print("Try Again")
       print("The output value is",b)
