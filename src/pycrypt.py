import sys
from os import path
import math
import time
import binascii
import base64
import binhex
import hashlib
import hmac
import quopri
import uu
import xdrlib


# console parameter check
'''
0   pycrypt.py
1   -e / -d
2   filepath 1
3   -o
4   filepath 2

'''

#TODO: add algorithms in algorithm class (in that "SWITCH-CASE")
#TODO: find out more dataencryptions
'''
Info:
    brute forcing
    key sizes
    block sizes

symmetric:
    info:
        same key
    des
    aes
    mars
    idea
    rc2
    rc4
    rc5
    rc6
    blowfish
    twofish
    threefish
    serpent
    base64


asymmetric:
    info:
        not same key
    diffie-hellman
    rsa
    elliptic curve

one way hash
    sha

other:
    transposition
        order

    substituition
        replace

    codebook

    other mathematics

'''

# How to add a new algorithm:
# 1. Append name to algoList
# 2. Add if statement to decode AND encode in Algorithm class
# 3. Add way to decode/encode that in that if statement


version = "0.1"

encrypt = True
fileI = None
fileO = None
input = None
output = None
hasOutput = False

# in lower
algoList = [
"base64",
"des"
]



if len(sys.argv) >= 3:
    if sys.argv[1] == "-e":
        pass

    elif sys.argv[1] == "-d":
        encrypt = False

    if path.exists(sys.argv[2]):
        fileI = open(sys.argv[2], "r")
        input = fileI.readlines()[0]
        fileI.close()
    else:
        print("Wrong Usage! The file doesn't exist")
        exit()

    #optional
    if len(sys.argv) == 5:
        if sys.argv[3] == "-o":
            hasOutput = True


#class that has different decode() and encode() on "type" in init
class Algorithm:
    #type corresponds to algolist
    type = None
    def __init__(self, type):
        this.type = type

    decode(input):
        output = "something"

        # the "SWITCH-CASE" for algorithms
        # HERE. do something with output
        if type == 1:
            #base64
            pass
        if type == 2:
            #des
            pass

        return output

    encode(input):
        output = "something"
        return output

print("pycrypt " + version + " by yungcxn")

print("Choose a " + ("Encryption" if encrypt else "Decryption")
    + " Algorithm by typing the corresponding number of the following list:")

#Do something with algoList to print it beautified
i = 0
for item in algoList:
    print(item + " : " + i)
    i+=1


OurAlgo = None
while(True):
    indexNumber = input("")
    indexIsNumber = indexNumber.isdigit()
    if indexIsNumber == False:
        print("Wrong Usage! Retry")

    elif int(indexNumber) < 0 && int(indexNumber) > len(algoList):
        print("Wrong Usage! Retry")

    else:
        OurAlgo = Algorithm(int(indexNumber))
        print("You've chosen: " + algoList[int(indexNumber)])
        break


print("Please wait...")

if encrypt:
    output = OurAlgo.encode(input)
elif encrypt == False:
    output = OurAlgo.decode(input)

print("Done!")
print("")

print(output)

if hasOutput:
    #if doesnt exist, then create else truncate
    fileO = open(sys.argv[4], "w+")
    fileO.write(output)
    fileO.close()
    print("Output is also at " + sys.argv[4])
