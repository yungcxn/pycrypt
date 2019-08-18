import sys
import os
import math
import platform

import time
import binascii
import base64
import binhex



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
"base32",
"base16"
]

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

if len(sys.argv) >= 3:
    if sys.argv[1] == "-e":
        pass

    elif sys.argv[1] == "-d":
        encrypt = False

    if os.path.exists(sys.argv[2]):
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
        self.type = type

    def decode(self, x):
        # the "SWITCH-CASE" for algorithms
        # HERE. do something with output
        #base64
        output = None
        if self.type == 0:
            output = base64.standard_b64decode(x)

        #base32
        if self.type == 1:
            output = base64.b32decode(x)

        #base16
        if self.type == 2:
            output = base64.b16decode(x)

        return output

    def encode(self, x):
        output = None
        if self.type == 0:
            output = base64.standard_b64encode(x)

        #base32
        if self.type == 1:
            output = base64.b32encode(x)

        #base16
        if self.type == 2:
            output = base64.b16encode(x)

        return output

print("pycrypt " + version + " by yungcxn")

print("Choose a " + ("Encryption" if encrypt else "Decryption")
    + " Algorithm by typing the corresponding number of the following list:")

#temps to indicate i=index , longest=number of "="
i = 0
longest = 0

#separator
print("\n")

#calc for topline
for item in algoList:
    toPrint = str(i) + " :: " + item
    if len(toPrint) > longest:
        longest = len(toPrint)
    i+=1

#topline
print("('x' to exit)")
print(longest * "=")

#reset
i = 0

#print and bottomline
for item in algoList:
    toPrint = str(i) + " :: " + item
    print(toPrint)
    i+=1

#bottomline
print(longest * "=")


#indicate algorithm instance
OurAlgo = None
#to continue if wrong usage, else break
while(True):
    indexNumber = raw_input("")
    if(indexNumber == "x"):
        exit()
    indexIsNumber = indexNumber.isdigit()
    if indexIsNumber == False:
        print("Wrong Usage! Retry")

    elif int(indexNumber) < 0 and int(indexNumber) > len(algoList):
        print("Wrong Usage! Retry")

    else:
        OurAlgo = Algorithm(int(indexNumber))
        print("You've chosen: " + algoList[int(indexNumber)])
        break

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
