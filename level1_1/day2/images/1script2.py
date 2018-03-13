import os
import shutil

# move files to the folder that created by its endswith
path = './'
files = os.listdir(path)

for f in files:
    if not f.endswith('.py'):
        if 'idea' or 'DS+Store' not in f:
            folder_path = './' + f.split('.')[-1]
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                shutil.move(f, folder_path)
            else:
                shutil.move(f,folder_path)