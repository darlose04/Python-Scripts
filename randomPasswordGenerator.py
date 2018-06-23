import random
import string

def randPass():

    password = list(random.choices(string.printable, k=15))
    str(password).replace(" ", "")

    return ''.join(password)


print(randPass())