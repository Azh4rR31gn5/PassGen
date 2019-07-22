# Hello this is a simple password generator tool
# 'PassGen' V 0.2b but still in beta version
# still have bugs
# sometime does not work as intended !!!

import random as r  #import random to be able to generate a random integer in a given range

print("           Hello Friend  " )
print("******** Coded by AzharREigns **********")
print(" ******* Version : 0.2b *******")
print()
print("     This is a 'simple' password generator    ")
print("   Use this generator to get some new and uncrackable password ")
print("  Use a good password manager to store it if it is difficult to remember !!")
print()

num = int(input("Input the number of password to be generated : "))

c = num +1

print()

if num !=0 :

 alpha = int(input("Input number of Uppercase alphabets : "))
 lower = int(input("Input number of Lowercase alphabets : "))
 digit = int(input("Input number of Digits : "))

 print()

 passwd = ""



 for i in range(0,num):

    x = r.randint(1, 7)  # assign random number between 1 to 6 to x

    if x == 1:
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        for l in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        for m in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        print(passwd)
        passwd = ""          # initialise passwd to get new value

    if x == 2:
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        for l in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        for m in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        print(passwd)
        passwd = ""

    if x == 3:
        for l in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        for m in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        print(passwd)
        passwd = ""

    if x == 4:
        for l in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        for m in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        print(passwd)
        passwd = ""

    if x == 5:
        for m in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        for l in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        print(passwd)
        passwd = ""

    if x == 6:
        for m in range(1,digit + 1):
            passwd += str(r.randint(0, 9))
        for k in range(1,alpha + 1):
            passwd += chr(r.randint(65, 90))
        for l in range(1,lower + 1):
            passwd += chr(r.randint(97, 122))
        print(passwd)
        passwd = ""

 print()
 print(num , "passwords successfully generated with", alpha ,"Uppercase and ", lower ,"Lowercase and ",digit,"Digits !!!!")
 print()
 print("      Thanks for using this generator !! ")

else:
 print()
 print("      No password will be generated !!!")
 print("      Bye Bye Bye !!!!")
