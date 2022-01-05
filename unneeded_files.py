import os


def size_of_files(folder):
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) > 10000:
                print(filename)


size_of_files('/Users/annatyrka/PythonPractice/')
