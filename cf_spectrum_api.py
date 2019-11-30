#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests, json, sys
from config import cf_accounts, timeout

#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class cfSpectrumApi(object):
    def __init__(self, email, key, app={}, timeout=5):
        self.__url   = "https://api.cloudflare.com/client/v4"
        self.__email = email
        self.__key   = key
        self.__app   = app
        self.__timeout = timeout
        self.__headers = {
            'X-Auth-Email': self.__email, 
            'X-Auth-Key':   self.__key, 
            'Content-Type': 'application/json'
        }

    def GetSpectList(self, zone_id):
        '''
            获取指定 zone_id 的app 列表
        '''
        url = f"{self.__url}/zones/{zone_id}/spectrum/apps"
        try:
            ret = requests.get(url, headers=self.__headers, verify=False, timeout=self.__timeout)
        except Exception as e:
            return {"success": False, "result": None}
        else:
            return ret.json()

    def UpdateApp(self, zone_id, app):
        '''
            更新指定 zone_id 的app，app中必须包含id [97fc9e6bceb1418b9e1ea8550d23cbc6]，以及
            {'protocol': "tcp/8800",
            'dns': {'type': 'CNAME', 'name': 'lgrm2.bbqp5566.com'},
            'origin_direct': ['tcp://8.8.8.8:8800'],
            'ip_firewall': True,
            'proxy_protocol': True,}
        '''
        url  = self.__url + "/zones/%s" %zone_id + "/spectrum/apps/%s" %app['id']
        data = {
            'protocol': app['protocol'],
            'dns': app['dns'],
            # 'origin_direct': app['origin_direct'],
            'ip_firewall': app['ip_firewall'],
            'proxy_protocol': app['proxy_protocol'],
        }
        # CF 转发请求有两种，一种是直接转发到IP，一种转发到事先定义好的负载均衡组
        if 'origin_direct' in app:
            data['origin_direct'] = app['origin_direct']
        else:
            data['origin_dns'] = app['origin_dns']

        try:
            ret  = requests.put(url, headers=self.__headers, data=json.dumps(data), verify=False, timeout=self.__timeout)
        except Exception as e:
            return {"success": False, "result": None}
        else:
            return ret.json()

    def createApp(self, zone_id, app):
        '''
            新增指定 zone_id 的app，app中必须包含id [97fc9e6bceb1418b9e1ea8550d23cbc6]，以及
            {'protocol': "tcp/8800",
            'dns': {'type': 'CNAME', 'name': 'lgrm2.bbqp5566.com'},
            'origin_direct': ['tcp://8.8.8.8:8800'],
            'ip_firewall': True,
            'proxy_protocol': True,}
        '''
        url  = self.__url + "/zones/%s" %zone_id + "/spectrum/apps"
        data = {
            'protocol': app['protocol'],
            'dns': app['dns'],
            'origin_direct': app['origin_direct'],
            'ip_firewall': True,
            'proxy_protocol': True,
        }
        try:
            ret  = requests.post(url, headers=self.__headers, data=json.dumps(data), verify=False, timeout=self.__timeout)
        except Exception as e:
            return {"success": False, "result": None}
        else:
            return ret.json()

    def CreateIpfirewall(self, zone_id, ip, mode="block", notes="新增规则"):
        '''
            添加ip 防火墙规则，主要应该是block IP
            添加的防火墙规则，是按当前主域名来吧，不特定指某一子域名，即 "this website" 不是 "All websites in account"
            mode: block, challenge, whitelist, js_challenge
        '''
        url = self.__url + "/zones/%s" %zone_id + "/firewall/access_rules/rules"
        data = {
            "mode": mode,
            "configuration": {
                    "target": "ip",
                    "value": ip,
                },
            "notes": "%s: %s" %(mode, notes),
        }
        try:
            ret  = requests.post(url, headers=self.__headers, data=json.dumps(data), verify=False, timeout=self.__timeout)
        except Exception as e:
            print (str(e))
            return {"success": False, "result": None}
        else:
            return ret.json()

if __name__ == "__main__":
    print ("no more")