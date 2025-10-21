#! python3

import os, shutil

for foldername, subfolders, filenames in os.walk('.'):
    for name in filenames:
        if name[-4:] == '.txt':
            shutil.copy(name, 'new_folder')
