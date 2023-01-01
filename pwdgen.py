from random import choice
import string
import time
import json

nums = string.digits

pwdList = []
pwdDigit = input("Digits of password:\n")
pwdAmount = input("How much passwords:\n")
pwdCreated = 0
pwdFinal = []

while pwdCreated < (int(pwdAmount)):
    pwd = ''.join(choice(nums) for _ in range(int(pwdDigit)))

    for num in str(pwd):
        pwdList.append(num)

    pwdFinal.append(str(pwdList))
    
    pwdList = []

    pwdCreated += 1

pwdJson = json.dumps(pwdFinal, indent=4)

pwdFile = open("password.json", "w")
pwdFile.write(pwdJson)
pwdFile.close()