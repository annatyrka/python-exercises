# Searches for files with a given prefix in a single folder
# Such as: spam001.txt, spam002.txt
# Locates any gaps in the numbering
# Renames all the later files to close this gap

import os
import shutil
import re


def filling_gaps(folder, prefix):
    p = os.path.abspath(folder)

    file_regex = re.compile(prefix+'(\d{1,})(.\w{3})')
    file_list = sorted([filename for filname in os.listdir(folder)] if file_regex.match(file_name)])
    print(file_list)

    for
