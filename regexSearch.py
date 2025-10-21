import re, os

for filename in os.listdir():
    if filename[-4:] == '.txt':
        fileObj = open(filename)
        content = fileObj.readlines()
        print('Enter a regular expression to find a line in ' + filename + ':')
        regex = re.compile('^' + input() + '(\n)?$')
        for i in range(len(content)):
            mo = regex.search(content[i])
            if mo != None:
                print('Found!')
