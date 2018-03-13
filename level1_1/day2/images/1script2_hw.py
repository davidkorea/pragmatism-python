import os
import shutil

# Q: move jpg,png,gif to folder images, others to documents folder
# A: 1. origin_folder_path_list
#    2. scan each folder and move files to new folder as conditions
#       accoding to file's endswith
#    3. after moving delete old folder

path = './'
files = os.listdir(path)
images_folder = './'+'images'
documents_folder = './'+'documents'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)
print(files)

origin_folder_path_list = []
for item in files:
    if item not in ['documents','images','DS_Store','idea']:
        if not item.endswith('.py'):
            origin_folder_path_list.append('./'+item)
print(origin_folder_path_list)

for path in origin_folder_path_list:
    sub_files = os.listdir(path)
    for s_f in sub_files:
        s_f_endswith = s_f.split('.')[-1]
        s_f_path = './' + str(s_f_endswith)
        if s_f_endswith in ['jpg','png','gif']:
            shutil.copy(os.path.join(s_f_path,s_f),images_folder)
        else:
            shutil.copy(os.path.join(s_f_path,s_f),documents_folder)
    shutil.rmtree(path)


# RESET
# For texting the codes above
for reset_item in [images_folder,documents_folder]:
    if os.path.exists(reset_item):
        for f1 in os.listdir(reset_item):
            folder_path = './' + f1.split('.')[-1]
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                shutil.copy(os.path.join(reset_item,f1),folder_path)
            else:
                shutil.copy(os.path.join(reset_item,f1),folder_path)
        shutil.rmtree(reset_item)
