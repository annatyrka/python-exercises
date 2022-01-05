# Copies an entire folder and its content into a ZIP file that filename increments

import zipfile
import os


def backup_to_zip(folder):

    folder = os.path.abspath(folder)    # enure the folder is absolute

    # Figure out the filename this code should use based on what files already exist

    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create a ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder

    for folder_name, subfolders, filenames in os.walk(folder):
        print('Adding files in {folder_name}...')
        backup_zip.write(folder_name)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if file_name.startswith(new_base) and file_name.endswith('.zip')":
                continue    # don't back up the backup ZIP files
            backup_zip.write(os.path.join(folder_name, filename))
        backup_zip.close()
        print('Done.')
