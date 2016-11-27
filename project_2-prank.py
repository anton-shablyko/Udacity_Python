''' task:
1- read files from folder
2 - strip numbers
3 - save files with the new filenames'''

import os

path = (os.getcwd()) + '/prank/'
result_path = (os.getcwd()) + '/result/'

y = os.listdir(path)
for filename in y:
    new_filename = ''.join([i for i in filename if not i.isdigit()])
    os.rename(path + filename, result_path + new_filename)
    print('Original name: {}, New name: {}'.format(filename, new_filename))