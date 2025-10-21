import os

for foldername, subfolders, filenames in os.walk('C:\\Users\\fabio'):
    for file in filenames:
        fileAbsPath = os.path.abspath(foldername + '\\' + file)
        if os.path.getsize(fileAbsPath) > 100000000:
            print(fileAbsPath)
