def createid_randomizer():
    # Generates a random userid and returns as output
    import string    
    import random 
    count = 10 
    generated_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = count))    
    return generated_id


def secret_key():
    # Generates a secret key to connect to the database and returns as output
    from cryptography import fernet
    key= fernet.Fernet.generate_key()
    return key

def trade_hashid():
    import sys
    max_threshold= sys.maxsize
    from random import randint
    hash_id= randint(1, max_threshold)
    return hash_id

