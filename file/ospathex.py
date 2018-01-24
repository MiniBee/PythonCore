import os


for temdir in ('/home/phy/data', r'c:\tmep'):
    if os.path.isdir(temdir):
        break
    else:
        print('no temp directory available..')
        temdir = ''
