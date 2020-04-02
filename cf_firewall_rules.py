#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys

from config          import *
from cf_firewall_rules_api import CfFirewallRulesApi

#禁用安全请求警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

### 给cf 域名添加黑名单 ###
# for customer in manage:
#     if customer in ['alcp3.com', '', '']:
#         info = manage[customer]
#         mode = 'block'
#         csa = cfSpectrumApi(info['email'], info['key'])
#         for ip in info['whitelist']:
#             if '/' in ip:
#                 target = 'ip_range'
#             else:
#                 target = 'ip'
#             # result = csa.CreateIpfirewall(info['zone_id'], ip, mode=mode, notes=f"cc")
#             result = csa.CreateIpfirewall(info['zone_id'], ip, mode=mode, notes=f"{customer}: cc", target=target)
#             print (result)

### 给cf 域名设置防火墙规则 ###
customer = 'alcp3.com'
info = manage[customer]

cfra = CfFirewallRulesApi(info['email'], info['key'])

# print(cfra.get_firewall_rules_list(info['zone_id']))
data = cfra.get_firewall_rules_list(info['zone_id'], description='CC-03: www.alcp3.com',)

print(data['data']['result'])

# data['data']['result'][0]['filter']['expression'] = \
# 'http.host contains "alcp3.com" and http.request.uri contains "/login/login_ok?agname=" and http.user_agent eq "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"'

# # 'http.host contains "alcp3.com" and http.request.uri contains "/login/login_ok?agname=" and (http.user_agent eq "Mozilla/4.0(compatible; MSIE 9.0; Windows NT 6.1)" or http.user_agent eq "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)" or http.user_agent eq "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)")'

# data['data']['result'][0]['description'] = "CC-03: www.alcp3.com"
# data['data']['result'][0]['filter']['paused'] = False
# data['data']['result'][0]['filter']['description'] = "Restrict access from these browsers"
# data['data']['result'][0]['filter']['ref'] = "FIL-003"
# del data['data']['result'][0]['created_on']
# del data['data']['result'][0]['modified_on']
# # del data['data']['result'][0]['paused']
# # del data['data']['result'][0]['description']
# # del data['data']['result'][0]['action']
# cfra.update_firewall_rules(info['zone_id'], rules=data['data']['result'])


# filters = [{
#     "id": data['data']['result'][0]['filter']['id'],
#     "paused": False,
#     "expression": 'http.host contains "alcp3.com" and http.request.uri contains "/login/login_ok?agname=" and http.user_agent eq "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"',
#     "description": "Restrict access from these browsers"
# }]

# cfra.update_firewall_rules_filters(info['zone_id'], filters=filters)