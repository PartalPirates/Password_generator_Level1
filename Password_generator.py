import random
import string

Alphabet1=string.ascii_letters
Alphabet1=string.ascii_lowercase
Alphabet3=string.ascii_uppercase
marks=string.punctuation
Choices=Alphabet1+marks
password=[]
Range=int(input("Enter a range for your Password :"))
for i in range(Range):
    password.append(random.choice(Choices))
print("your password is : ", password)



