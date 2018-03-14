import os
import shutil
import datetime
import time

def scan_file():
    files = os.listdir()
    for f in files:
        if f.endswith('.zip'):
            return f

def unzip(f):
    folder_name = f.split('.')[0]
    unzip_path = './' + folder_name
    if not os.path.exists(unzip_path):
        os.makedirs(unzip_path)
        shutil.unpack_archive(f, unzip_path)
    else:
        # in case of duplicated folder name
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        d = datetime.datetime.now().day
        h = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        s = datetime.datetime.now().second
        unzip_path_i = unzip_path+'_'+str(y)+str(m)+str(d)+str(h)+str(min)+str(s)
        os.makedirs(unzip_path_i)
        shutil.unpack_archive(f, unzip_path_i)

def delete(f):
    os.remove(f)

while True:
    zip_file = scan_file()
    if zip_file:
        unzip(zip_file)
        delete(zip_file)
    time.sleep(3)