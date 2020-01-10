#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests

class SuperSign(object):
    '''
        超级签，通过程序接口，查看一些基本信息
    '''
    def __init__(self, api):
        self.__api = api
        self.__timeout = 5

    def get_data(self):
        try:
            ret = requests.get(self.__api, verify=False, timeout=self.__timeout)
            data = ret.json()['data']
        except Exception as e:
            # raise e
            print (str(e))
            return {'code': 500, 'msg': '数据获取失败: '+str(e), 'data': None}
        else:
            return {'code': 0, 'msg': '数据获取成功', 'data': data}