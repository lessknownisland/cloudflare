#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys

from config          import *
from cf_spectrum_api import cfSpectrumApi
#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#cf接口，账户参数
cf_url = "https://api.cloudflare.com/client/v4/zones"
email  = "L5yirencp@gmail.com"
key    = "5321b5c5022b60107a9e5ad295539c58ee551"

# zone_id = "689438eb0e73fd72cdbf01067c22575d" #bbqp5566.com zone_id
zone_id = "9c7c2edc108019e82c6272677ed6ccf3" #appifc.com zone_id

# #requests参数
# headers = {'X-Auth-Email': email, 'X-Auth-Key': key, 'Content-Type': 'application/json'}

#给cf 后台域名添加白名单
for customer in manage:
    if customer == "vgsport":
        info = manage[customer]
        csa = cfSpectrumApi(info['email'], info['key'])
        for ip in info['whitelist']:
            result = csa.CreateIpfirewall(info['zone_id'], ip, mode='whitelist', notes="vgsport 后台白名单")
            print (result)
            # break

sys.exit(0)

#获取api 接口
csa = cfSpectrumApi(email, key)

#获取指定域名的applist
#print (csa.GetSpectList(zone_id))
appList = csa.GetSpectList(zone_id)
if 'result' not in appList.keys(): 
    print ("获取结果失败：%s" %appList)
    sys.exit(1)
else:
    appList = appList['result']
if not appList: sys.exit(1)

#block 非法IP
# print (csa.CreateIpfirewall(zone_id, "192.168.100.2", notes="非法请求tcp"))
# sys.exit(0)

for app in appList:
    # print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
    # continue
    # sys.exit()
    # if app['protocol'] == "tcp/8800":
    #     print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
    #     # if app['dns']['name'] == "lgrm2.appifc.com":
    #     #     app['origin_direct'] = ['tcp://8.8.8.8:8800']
    #     #     print (csa.UpdateApp(zone_id, app))
    # continue

    if app['dns']['name'] == "lgrm2.appifc.com":
        # zone_id = "ea898577a1186e8c8a5d3e7fb7ab35d3"
        # app['dns']['name'] = "lgrm.bbqp0555.com"
        # app['origin_direct'] = [app['origin_direct'][0].replace("52.128.245.125", "47.244.106.52")]
        #app['dns']['name'] = "lgrm5.appifc.com"
        #app['origin_direct'] = [app['origin_direct'][0].replace("47.75.140.240", "52.128.245.125")]
        app['proxy_protocol'] = True
        print (csa.UpdateApp(zone_id, app))
        continue
    else:
        continue
        
    if app['protocol'] == "tcp/8800" and app['dns']['name'] in ["lgrm3.bbqp5566.com", "lgrm4.bbqp5566.com"]:
        # app['origin_direct'] = ['tcp://8.8.8.8:8800']
        app['origin_direct'] = [
                'tcp://47.244.106.52:8800',
                'tcp://216.118.228.180:8800',
                'tcp://216.118.245.220:8800',
                'tcp://180.178.32.100:8800',
                'tcp://52.128.245.124:8800',
                'tcp://182.16.117.180:8800',
                ]
        print (csa.UpdateApp(zone_id, app))
        continue

    if app['dns']['name'] not in [""]:
        if app['protocol'] == "tcp/8800":
            print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
            # print (app)
            # app['origin_direct'] = ['tcp://8.8.8.8:8800']
            # updateApp(app)
    # updateApp(app)
    # continue
    # print (app)
    # break
    # print (app['id'], app['dns']['name'], app['protocol'], app['origin_direct'], app['ip_firewall'], app['proxy_protocol'])
    