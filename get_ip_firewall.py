#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import datetime
import json
import sys

from config          import *
from cf_spectrum_api import cfSpectrumApi

for customer in ['venetian', 'ali', 'gd']:
    info = manage[customer]
    csa = cfSpectrumApi(info['email'], info['key'])
    for ip in info['whitelist']:
        get_ip_result = csa.GetIpfirewall(info['zone_id'], ip)
        if get_ip_result['result']:
            for rule in get_ip_result['result']:
                # if '175.176.3' not in rule['configuration']['value']:
                #     continue
                c_time = datetime.datetime.strptime(rule['created_on'][:-4], '%Y-%m-%dT%H:%M:%S.%f') + datetime.timedelta(hours=8)
                c_time = c_time.strftime('%Y-%m-%d %H:%M:%S')
                if rule['scope']['type'] == 'zone':
                    name = rule['scope']['name']
                elif rule['scope']['type'] == 'organization':
                    name = '账号所有域名'
                else:
                    name = '未知'
                detail = "\n".join([
                    # f"\n",
                    f"-"*100,
                    f"ID: {rule['id']}",
                    f"创建时间: {c_time}",
                    f"类型: {rule['mode']}",
                    f"IP 类型: {rule['configuration']['target']}",
                    f"IP: {rule['configuration']['value']}",
                    f"备注: {rule['notes']}",
                    f"主域名: {name}",
                    # f"-"*100,
                    # f"\n",
                    # f""
                ])
                # print(rule)
                print(detail)
            print('\n')
            print('='*100)
            print(f"total: {len(get_ip_result['result'])}")
            print('='*100)
        # print(get_ip_result['result'])