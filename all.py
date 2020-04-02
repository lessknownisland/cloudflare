#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import datetime
import json
import sys

from config          import *
from cf_spectrum_api import cfSpectrumApi

for customer in manage:
    info = manage[customer]
    mode = 'whitelist'
    csa = cfSpectrumApi(info['email'], info['key'])
    # ip = '119.28.193.77'
    ip = '180.191.155.138'
    
    get_ip_result = csa.CreateIpfirewall(info['zone_id'], ip, mode=mode, notes=f"{customer}: 后台")

    if not get_ip_result['success']:
        detail = "\n".join([
                # f"\n",
                f"-"*100,
                f"业主: {customer}",
                f"失败: {get_ip_result['errors']}",
                # f"-"*100,
                # f"\n",
                # f""
            ])

    if get_ip_result['result']:
        rule = get_ip_result['result']
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
            f"IP: {rule['configuration']['value']}",
            f"备注: {rule['notes']}",
            f"主域名: {name}",
            # f"-"*100,
            # f"\n",
            # f""
        ])
    print(detail)