# This is an example issue.py with a paired parameters.txt that cracks MD5 hashes (Specifically, the MD5 hash of "password")
# Real issue.py must follow the specifications:
# 1: Main function must be called 'compute'
# 2: Main function must accept a single string value as arguments and parse the input itself
# 3: Main function must return a string value
# 4: (Optional) Use only standard modules for portability

import hashlib
import random
import string

def compute(intake):
    list = intake.split(", ")
    list[1] = int(list[1].strip())
    hash = ""
    random_string = ""
    while (hash != list[0]):
        random_string = "".join(random.choices(string.ascii_letters, k=list[1]))
        hash = hashlib.md5(random_string.encode("utf-8")).hexdigest()
    return random_string