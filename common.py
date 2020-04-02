#!/usr/bin/env python3
#-_- coding: utf-8 -_-
import platform
import random
import string

def get_random_s(num):
    '''
        获取一个随机的 num 位的字符串
    '''
    return "".join(random.sample(string.ascii_letters + string.digits, num))

if __name__ == '__main__':
    print (platform.python_version())
    print ("%s is just a common file." %__file__)
