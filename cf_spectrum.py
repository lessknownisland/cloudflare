#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys

from config          import *
from cf_spectrum_api import cfSpectrumApi
#禁用安全请求警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#cf接口，账户参数
cf_url = "https://api.cloudflare.com/client/v4/zones"
email  = "L5yirencp@gmail.com"
key    = "5321b5c5022b60107a9e5ad295539c58ee551"

# zone_id = "689438eb0e73fd72cdbf01067c22575d" #bbqp5566.com zone_id
zone_id = "9c7c2edc108019e82c6272677ed6ccf3" #appifc.com zone_id

# #requests参数
# headers = {'X-Auth-Email': email, 'X-Auth-Key': key, 'Content-Type': 'application/json'}

### 给cf 后台域名添加白名单 ###
for customer in manage:
    if customer == 'uc':
        info = manage[customer]
        mode = 'whitelist'
        csa = cfSpectrumApi(info['email'], info['key'])
        for ip in info['whitelist']:
            # result = csa.CreateIpfirewall(info['zone_id'], ip, mode=mode, notes=f"cc")
            result = csa.CreateIpfirewall(info['zone_id'], ip, mode=mode, notes=f"{customer}: 后台")
            print (result)
            # if 'errors' in result.keys() and len(result['errors']) != 0:
            #     if  result['errors'][0]['message'] == 'firewallaccessrules.api.duplicate_of_existing':
            #         # print (f"{info['zone_id']}, {ip}")
            #         # print (csa.GetIpfirewall(info['zone_id'], ip)['result'][0])
            #         get_ip_result = csa.GetIpfirewall(info['zone_id'], ip)
            #         if 'result' in get_ip_result.keys() and len(get_ip_result['result']) != 0:
            #             rule_id = get_ip_result['result'][0]['id']
            #             print (csa.DeleteIpfirewall(info['zone_id'], rule_id))
            # break
# sys.exit()

# # 获取api 接口
# csa = cfSpectrumApi(email, key)

# ### 获取指定域名的applist ###
# # print (csa.GetSpectList(zone_id))
# appList = csa.GetSpectList(zone_id)
# if 'result' not in appList.keys(): 
#     print (f"获取结果失败：{appList}")
#     sys.exit(1)
# else:
#     appList = appList['result']
# if not appList: sys.exit(1)

# ### block 非法IP ###
# # print (csa.CreateIpfirewall(zone_id, "192.168.100.2", notes="非法请求tcp"))
# # sys.exit(0)

# for app in appList:
#     ### 打印 当前获取到的app 转发详情 ###
#     # if 'origin_direct' in app:
#     #     print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
#     # else:
#     #     print (app)
#     # continue
#     # sys.exit()

#     ### 针对 8800 端口做指定的调整更新 ###
#     # if app['protocol'] == "tcp/8800":
#     #     print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
#     #     # if app['dns']['name'] == "lgrm2.appifc.com":
#     #     #     app['origin_direct'] = ['tcp://8.8.8.8:8800']
#     #     #     print (csa.UpdateApp(zone_id, app))
#     # continue

#     ### 针对 指定的域名 做指定的调整更新 ###
#     if app['dns']['name'] == "lgrm2.appifc.com":
#         # zone_id = "ea898577a1186e8c8a5d3e7fb7ab35d3"
#         # app['dns']['name'] = "lgrm.bbqp0555.com"
#         # app['origin_direct'] = [app['origin_direct'][0].replace("52.128.245.125", "47.244.106.52")]
#         #app['dns']['name'] = "lgrm5.appifc.com"
#         #app['origin_direct'] = [app['origin_direct'][0].replace("47.75.140.240", "52.128.245.125")]
#         app['proxy_protocol'] = False
#         print (csa.UpdateApp(zone_id, app))
#         # break
#         continue
#     else:
#         continue
        
#     ### 针对 指定的域名以及指定的端口 做指定的调整更新 ###
#     if app['protocol'] == "tcp/8800" and app['dns']['name'] in ["lgrm3.bbqp5566.com", "lgrm4.bbqp5566.com"]:
#         # app['origin_direct'] = ['tcp://8.8.8.8:8800']
#         app['origin_direct'] = [
#                 'tcp://47.244.106.52:8800',
#                 'tcp://216.118.228.180:8800',
#                 'tcp://216.118.245.220:8800',
#                 'tcp://180.178.32.100:8800',
#                 'tcp://52.128.245.124:8800',
#                 'tcp://182.16.117.180:8800',
#                 ]
#         print (csa.UpdateApp(zone_id, app))
#         continue

#     if app['dns']['name'] not in [""]:
#         if app['protocol'] == "tcp/8800":
#             print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
#             # print (app)
#             # app['origin_direct'] = ['tcp://8.8.8.8:8800']
#             # updateApp(app)
#     # updateApp(app)
#     # continue
#     # print (app)
#     # break
#     # print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
    