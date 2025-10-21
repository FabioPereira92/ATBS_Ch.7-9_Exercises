import re

def strongPasswordDetection(password):
    passwordRegex1 = re.compile(r'^[a-zA-Z0-9]{8,}$')
    passwordRegex2 = re.compile(r'\d+')
    passwordRegex3 = re.compile(r'[a-z]+')
    passwordRegex4 = re.compile(r'[A-Z]+')
    mo1 = passwordRegex1.search(password)
    mo2 = passwordRegex2.search(password)
    mo3 = passwordRegex3.search(password)
    mo4 = passwordRegex4.search(password)
    if mo1 != None and mo2 != None and mo3 != None and mo4 != None:
        print('The password is strong')       
    else:
        print('The password isn\'t strong')

