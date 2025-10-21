import re

def regexVersionOfStrip(string, chars=None):
    if chars != None:
        regex1 = re.compile(r'^' + (chars) + '+')
        regex2 = re.compile((chars) + '+$')
    else:
        regex1 = re.compile(r'^(\s+)')
        regex2 = re.compile(r'(\s+)$')
    newString = regex1.sub('', string)
    newString2 = regex2.sub('', newString)
    return newString2
