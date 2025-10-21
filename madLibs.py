import re

fileObj = open('textExample.txt', 'r')
content = fileObj.read()
fileObj.close()
regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
findsList = regex.findall(content)
for i in findsList:
    if i == 'ADJECTIVE':
        print('Enter an adjective:')
        answer1 = input()
        content = re.compile('ADJECTIVE').sub(answer1, content)
    elif i == 'NOUN':
        print('Enter a noun:')
        answer2 = input()
        content = re.compile('NOUN').sub(answer2, content)
    elif i == 'ADVERB':
        print('Enter an adverb:')
        answer3 = input()
        content = re.compile('ADVERB').sub(answer3, content)
    elif i == 'VERB':
        print('Enter a verb:')
        answer4 = input()
        content = re.compile('VERB').sub(answer4, content)
print(content)
fileObj = open('textExampleAnswer.txt', 'w')
fileObj.write(content)
fileObj.close()
