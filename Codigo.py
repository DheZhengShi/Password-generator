import random

#some input
length = input("Insertar un número entero positivo: ")
if not ValueError(length):
  length = int(length)
 #generator
  def create_password(pass_length):
   typing= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
   password = ""

   for i in range(pass_length):
    password += random.choice(typing)
   return print(password)
  create_password(length)
else: 
  print("Ese no es un número")

#Investigué un poco por mi cuenta para esto.
