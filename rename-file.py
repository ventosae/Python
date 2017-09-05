import os
import re
def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Project_Science\Python\Tasks\Prank")
    os.chdir(r"C:\Project_Science\Python\Tasks\Prank")
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, re.sub("[0-9]"," ", file_name))
rename_files()
