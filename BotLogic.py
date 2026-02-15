import random

def gen_pass(pass_length = 8):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Орёл"
    else:
        return "Решка"