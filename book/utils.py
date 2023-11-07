import random

numb = "1234567890"
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ass = numb * 9 + alph

def new_payment_id(id, n=12):
    dt = len(str(id))
    key = ""
    for j in range(n-dt):
        k = random.randint(0, len(ass)-2)
        key += ass[k]
    return key + str(id)