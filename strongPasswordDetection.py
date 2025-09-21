import re

def StrongPasswordDetection(password):
    passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    mo = passwordRegex.search(password)
    if mo == None:
        print('The password isn\'t strong')
    else:
        print('The password is strong')

StrongPasswordDetection('23kldsSD')
StrongPasswordDetection('abcdef')
StrongPasswordDetection('ABCDEFGH')
StrongPasswordDetection('abc12345')
