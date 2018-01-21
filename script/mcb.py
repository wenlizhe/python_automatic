#! /usr/bin/env python3
# coding: utf-8
# date: 20180120
import os
import re


path = '../test_dir'


# 遍历指定目录，显示目录下的所有文件名
def each_file(filepath):
    # pathDir = os.listdir(filepath)
    file_list = []
    for parent, dirnames, filenames in os.walk(filepath):
        for filename in filenames: 
            file_list.append(os.path.join(parent, filename))
        for dirname in dirnames:
            os.path.join(parent, dirname)
    return file_list


# 读取文件内容并打印
def read_file(filename):
    for f in filename:
        if f.endswith('.txt'):
            try:
                file = open(f, encoding='utf-8')
                find = file.read()
                mail = re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*"
                                  r"@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?", find)
                print(mail)
            except UnicodeDecodeError as e:
                raise
            finally:
                file.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
def write_fiel(filename):
    pass


if __name__ == '__main__':
    filename = each_file(path)
    read_file(filename)
