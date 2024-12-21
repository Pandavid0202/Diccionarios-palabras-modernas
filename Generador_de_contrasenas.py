import random

strings = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
           
lg = int(input("introduce la longitud de tu contraseña"))

contraseña = ""   

for i in range(lg):
    contraseña = contraseña + random.choice(strings)
    

print("esta es tu contraseña",contraseña)
