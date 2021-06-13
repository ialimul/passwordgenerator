import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFFGHIJKLMNOPQRSTUVWXYZ123456789~!@#$%^&*()_+/-.{[]:|?/<>\""

while 1:
    password_leng = int(input("Type the length of your password:"))
    password_count = int(input("Total number of passwords you want to generate:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_leng):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is the password:", password)