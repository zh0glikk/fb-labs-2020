from RSA.rsa import *
import rsa
from RSA.crypto_math import *
import json
import requests

if __name__ == '__main__':
    rsa1 = rsa.RSA(12345, 512)
    keygen_request = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512')
    cookie = keygen_request.cookies
    cookie_name = cookie.keys()[0]
    cookie_value = cookie.values()[0]
    print("ім'я cookie: {}".format(cookie_name))
    print("значення cookie: {}".format(cookie_value))

    # p, q, _, __ = generate_key_pairs(256)
    # rsa = RSA(p, q)