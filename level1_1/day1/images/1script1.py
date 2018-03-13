import os

path = '/Users/osx/Desktop/pragmatism-python/level1_1/day1/images'
files = os.listdir(path)

for f in files:
    if f.endswith('png') and 'fish' in f:
        print('found it!'+f)