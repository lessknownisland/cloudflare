#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys
import random

from config import cf_accounts, timeout
from logger import logger

#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class cfSpectrumApi(object):
    def __init__(self, email, key, app={}, timeout=5):
        self.url   = "https://api.cloudflare.com/client/v4"
        self.email = email
        self.key   = key
        self.app   = app
        self.timeout = timeout
        self.headers = {
            'X-Auth-Email': self.email, 
            'X-Auth-Key':   self.key, 
            'Content-Type': 'application/json'
        }

    def GetSpectList(self, zone_id):
        '''
            获取指定 zone_id 的app 列表
        '''
        url = f"{self.url}/zones/{zone_id}/spectrum/apps"
        try:
            ret = requests.get(url, headers=self.headers, verify=False, timeout=self.timeout)
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
        url  = f"{self.url}/zones/{zone_id}/spectrum/apps/{app['id']}"
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
            ret  = requests.put(url, headers=self.headers, data=json.dumps(data), verify=False, timeout=self.timeout)
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
        url  = self.url + "/zones/%s" %zone_id + "/spectrum/apps"
        data = {
            'protocol': app['protocol'],
            'dns': app['dns'],
            'origin_direct': app['origin_direct'],
            'ip_firewall': True,
            'proxy_protocol': True,
        }
        try:
            ret  = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False, timeout=self.timeout)
        except Exception as e:
            return {"success": False, "result": None}
        else:
            return ret.json()

    def CreateIpfirewall(self, zone_id, ip, mode="block", notes="新增规则", target="ip"):
        '''
            添加ip 防火墙规则，主要应该是block IP
            添加的防火墙规则，是按当前主域名来吧，不特定指某一子域名，即 "this website" 不是 "All websites in account"
            mode: block, challenge, whitelist, js_challenge
        '''
        url = self.url + "/zones/%s" %zone_id + "/firewall/access_rules/rules"
        data = {
            "mode": mode,
            "configuration": {
                    "target": target,
                    "value": ip,
                },
            "notes": "%s: %s" %(mode, notes),
        }
        try:
            ret  = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False, timeout=self.timeout)
        except Exception as e:
            print (str(e))
            return {"success": False, "result": None}
        else:
            return ret.json()

    def DeleteIpfirewall(self, zone_id, rule_id):
        '''
            删除ip 防火墙规则
        '''
        url = f"{self.url}/zones/{zone_id}/firewall/access_rules/rules/{rule_id}"
        try:
            ret  = requests.delete(url, headers=self.headers, verify=False, timeout=self.timeout)
        except Exception as e:
            print (str(e))
            return {"success": False, "result": None}
        else:
            return ret.json()

    def GetIpfirewall(self, zone_id, ip=None, mode=None, target='ip'):
        '''
            获取ip 防火墙规则，针对 IP
        '''
        page = 1
        url = f"{self.url}/zones/{zone_id}/firewall/access_rules/rules?per_page=1000"

        if mode:
            url += f"&mode={mode}"

        if ip:
            url += f"&configuration.value={ip}"

        try:
            ret  = requests.get(url, headers=self.headers, verify=False, timeout=self.timeout)
        except Exception as e:
            print (str(e))
            return {"success": False, "result": None}
        else:
            result = ret.json()
            while page < result['result_info']['total_pages']:
                ret  = requests.get(url, headers=self.headers, verify=False, timeout=self.timeout)
                result['result'] += ret.json()['result']
                page += 1
            return result

    def _send_req(self):
        '''
            发送 requests 请求
            code: 0 成功，500 失败
        '''
        self.__ret_data = {
            'code': 500,
            'msg': self.content
        }

        self.__req_id = ''.join(str(random.choice(range(10))) for _ in range(10)) # 对每一次请求，指定一个随机的10位数
        logger.info(f"""{self.content}: # 记录请求参数
            req_id: {self.__req_id}
            method: {self.method}
            url: {self.url_req}
            data: {self.data}
            headers: {self.headers}
        """)

        # 初始化请求的 session
        s = requests.Session()
        req = requests.Request(self.method, self.url_req,
            data=json.dumps(self.data),
            headers=self.headers
        )
        prepped = s.prepare_request(req)
        try:
            ret = s.send(prepped, verify=self.verify, timeout=self.timeout) # 发起请求
            
            self.__ret_data['code'] = 0
            if ret.status_code == 204: # 状态码 204，返回内容为空，例如 DELETE 证书的请求
                self.__ret_data['data'] = f"{self.content} 成功"
                logger.info(f"req_id: {self.__req_id} {self.__ret_data['data']}")

            else:
                app_ret = ret.json()
                self.__ret_data['data'] = app_ret
                self.__ret_data['msg']  = f"{self.content} 成功"

                if "success" not in app_ret.keys() or not app_ret["success"]:
                    self.__ret_data['msg']  = f"{self.content} 失败"
                    self.__ret_data['code'] = 500
                    logger.error(f"req_id: {self.__req_id} {self.__ret_data['msg']}: {self.url_req} :{str(app_ret)}")

                else:
                    logger.info(f"req_id: {self.__req_id} {self.__ret_data['msg']}: {self.url_req} :{str(app_ret)}")
        
        except Exception as e:
            self.__ret_data['msg'] = f"{self.content} 失败: {ret.text}"
            self.__ret_data['code'] = 500
            logger.error(f"req_id: {self.__req_id} {self.content} 失败: {self.url_req} : {str(e)}。返回错误: {ret.text}")

        return self.__ret_data

if __name__ == "__main__":
    print ("no more")