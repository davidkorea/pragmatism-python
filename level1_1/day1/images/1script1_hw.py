import os

path = '/Users/osx/Desktop/pragmatism-python/level1_1/day1/images'
files = os.listdir(path)

for f in files:
    if not f.endswith('gif') and 'project' in f or 'commercial' in f:
        print(f)