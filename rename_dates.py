# renames files from US format (MM-DD-YYYY) to European (DD-MM-YYYY)

import os
import shutil
import re

us_format = re.compile(r"""
^(.*?)           # all text before
((0|1)?\d)-      # one or two digits for the month
((0|1|2|3)?\d)-  # one or two digits for the day
((19|20)\d\d)      # four digits for the year
(.*?)$           # all text after the date
""", re.VERBOSE)
test = "03-30.2020.txt"
for us_filename in os.listdir('.'):
    mo = us_format.search(us_filename)

    if mo == None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + \
        month_part + '-' + year_part + after_part

    # Get the full, absolute file paths
    abs_working_dir = os.path.abspath('.')
    us_filename = os.path.join(abs_working_dir, us_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files
    print(f'renaming "{us_filename}" to "{euro_filename}"...')
    #shutil.move(us_filename, euro_filename)
