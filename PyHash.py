import os
import sys
import hashlib
from sys import platform
from banner import access
from menu import OPEN

from plat import check
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
# Created By: TheTechHacker            #
########################################


"""
This tool is for encrypting passwords or messages to hash 
it's meant for research purposes only
and any malicious usage of this tool is prohibited.


author :  TheTechHacker
"""



check.plat()



def md5():
    check.plat()
    access.Pyhash()
    access.description()
    while True:
        print "\033[1;32m"
        hash = raw_input("      Enter Text: ")
        print "\033[1;m"
        hash = hashlib.md5(hash)
        print (hash.hexdigest())


def sha1():
    check.plat()
    access.Pyhash()
    access.description()
    while True:
        print "\033[1;32m"
        sha1 = raw_input("      Enter Text: ")
        print "\033[1;m"
        hash = hashlib.sha1(sha1)
        print (hash.hexdigest())


def sha224():
    check.plat()
    access.Pyhash()
    access.description()
    while True:
        print "\033[1;32m"
        sha224 = raw_input("     Enter Text: ")
        print "\033[1;m"
        hash = hashlib.sha224(sha224)
        print (hash.hexdigest())


def sha256():
    check.plat()
    access.Hash()
    access.description()
    while True:
        print "\033[1;32m"
        sha256 = raw_input("     Enter Text: ")
        print "\033[1;m"
        hash = hashlib.sha256(sha256)
        print (hash.hexdigest())


def sha384():
    check.plat()
    access.Hash()
    access.description()
    while True:
        print "\033[1;32m"
        sha384 = raw_input("     Enter Text: ")
        print "\033[1;m"
        hash = hashlib.sha384(sha384)
        print (hash.hexdigest())


def sha512():
    check.plat()
    access.Hashed()
    access.description()
    while True:
        print "\033[1;32m"
        sha512 = raw_input("     Enter Text: ")
        print "\033[1;m"
        hash = hashlib.sha512(sha512)
        print (hash.hexdigest())



access.Pyhash()
access.description()
OPEN.menu()




print "\033[1;32m"
user = raw_input("ENTER: ")




if user == "1":
    print (md5())
elif user == "2":
    print (sha1())
elif user == "3":
    print (sha224())
elif user == "4":
    print (sha256())
elif user == "5":
    print (sha384())
elif user == "6":
    print (sha512())
elif user == "99":
    exit("\033[1;34m Exiting \033[1;m")
else:
    exit("\033[1;34m ERROR \033[1;m")