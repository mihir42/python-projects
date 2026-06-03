import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter pass len: "))

pswrd = ""
for i in range(length):
    pswrd = pswrd + random.choice(chars)

print(pswrd)