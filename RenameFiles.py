import os
'''
List files and rename them.
'''


folder = 'files/'
files = os.listdir(folder)

print files

for file in files:
    print 'Found file with name {0}'.format(file)

#rename files

for file in files :
    new_name = 'new' + file
    print 'rename {0} to {1}'.format(file, new_name)
    os.rename(folder+ file, folder + new_name)

print os.listdir(folder)

#replace file name new to old

print 'current folder is {0}'.format(os.getcwd())

for file in os.listdir(folder):
    old_file = file.replace('new', 'old')
    print 'changing name from {0} to {1}'.format(file, old_file)
    os.rename(folder + file, folder + old_file)

print os.listdir(folder)
