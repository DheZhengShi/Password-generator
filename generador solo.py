import random

#generador
def create_password(pass_length):
   typing= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
   password = ""

   for i in range(pass_length):
    password += random.choice(typing)
   return print(password)
create_password(100)
