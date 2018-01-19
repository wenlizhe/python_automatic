#!/usr/bin/python3
# date: 20180114

import re


def read_file():
    f = open('../test_dir/PhoneAndEmail.txt')
    r = f.read()
    return r


def is_phone_or_email(f):
    # phone_num_regex = re.compile(r'\d{11}')
    num = re.findall(r'\d{11}', f)
    mail = re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+"
                      r"[\w](?:[\w-]*[\w])?", f)
    return num, mail


if __name__ == '__main__':
    # for i in range(len(message)-12):
    #     chunk = message[i:i+12]
    #     if is_phone_num(chunk):
    #         print(is_phone_num(chunk))
    file = read_file()
    result = is_phone_or_email(file)
    print(result[0])
