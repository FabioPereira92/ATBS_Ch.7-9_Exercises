import re, shutil, os

regex = re.compile('^spam(\d\d\d)\.txt$')

filesList = os.listdir('.')

numbersList = []

for i in range(len(filesList)):
    mo = regex.search(filesList[i])
    if mo != None:
        numbersList.append(int(filesList[i][4:7]))
    
for i in range(len(numbersList) - 1):
    if numbersList[i+1] > numbersList[i] + 1:
        numbersList[i+1] = numbersList[i] + 1

for i in range(len(numbersList)):
    if len(str(numbersList[i])) == 1:
        numbersList[i] = '00' + str(numbersList[i])
    elif len(str(numbersList[i])) == 2:
        numbersList[i] = '0' + str(numbersList[i])
    else:
        numbersList[i] = str(numbersList[i])

spamFileList = []

for i in range(len(filesList)):
    mo = regex.search(filesList[i])
    if mo != None:
        spamFileList.append(filesList[i])

for i in range(len(spamFileList)):
    shutil.move('.\\' + spamFileList[i], '.\\' + 'spam' + numbersList[i] + '.txt')

    
