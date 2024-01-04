import random
import string

print('This program prints password.')

length = int(input('\nEnter the length of password: '))                      

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

all = lowercase + uppercase + number + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)