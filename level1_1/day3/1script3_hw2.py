import os
from shutil import make_archive
import time

image_path = './image'
output_path = './output'

archive_count = 0

while True:

    files = os.listdir(image_path)

    if len(files)>=5:
        archive_count = archive_count+1
        archive_path = output_path+'/'+'archive'+str(archive_count)
        make_archive(archive_path,'zip',image_path)
        for f in files:
            os.remove(image_path+'/'+f)
    time.sleep(1)
    # print(archive_count)