import os
import shutil


def selective_copy(folder, destination):
    # returns abolute path in case relative path is passed
    folder = os.path.abspath(folder)
    print(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        #print(f'The current folder is {foldername}')
        # for subfolder in subfolders:
        #print(f'SUBFOLDER of {foldername} is: {subfolder}')
        for filename in filenames:
            #print(f'FILE INSIDE {foldername} is {filename}')
            if filename.endswith('.txt'):
                print(f'Copying {filename}... to {destination}')
                shutil.copy(os.path.join(foldername, filename), destination)

    print('Done.')


selective_copy(
    'test/', '/Users/annatyrka/PythonPractice/Selective_Copy/')
