#! /usr/bin/env python3
# coding: utf-8
import shutil
import os
import zipfile
import logging
logging.basicConfig(level-logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
# for f in os.listdir():
#     if f.endswith('.py'):
#         print(f)

# for foldername, subfolders, filenames in os.walk('./'):
#     print(foldername, subfolders, filenames)

os.chdir('../test_dir/')
tempzip = zipfile.ZipFile('HiChat-master-master.zip')
print(tempzip.namelist())