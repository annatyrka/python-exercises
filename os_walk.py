import os


def os_walk(folder):

    # returns abolute path in case relative path is passed
    folder = os.path.abspath(folder)
    print(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'The current folder is {foldername}')
        for subfolder in subfolders:
            print(f'SUBFOLDER of {foldername} is: {subfolder}')
        for filename in filenames:
            print(f'FILE INSIDE {foldername} is {filename}')

    print('Done.')


os_walk('test/')
