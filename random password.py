import string
import random

def randompassword():
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 6
    return "".join(random.choice(char)for x in range(size,20))


n = 0
while n<10:
    print(randompassword())
    n+=1

    
