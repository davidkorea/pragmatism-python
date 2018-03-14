# scan -- unzip -- delete
import os
import shutil

def scan_file():
    for f in os.listdir(): #由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    folder_name = f.split('.')[0]
    target_path = './' + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f,target_path)


def delete(f):
    os.remove(f)


while True:
    zip_file = scan_file()
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)


