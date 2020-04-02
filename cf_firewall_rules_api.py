#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests, json, sys
from config import cf_accounts, timeout
from cf_spectrum_api import cfSpectrumApi

#禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CfFirewallRulesApi(cfSpectrumApi):

    def get_firewall_rules_list(self, zone_id, page=1, per_page=100, **dict_args):
        '''
            获取指定 zone_id 的firewall rules 列表
            参数：
            id : Firewall Rule identifier
            description : Case-insensitive search in description
            action : block, challenge, whitelist, js_challenge
            paused : Whether this firewall rule is currently paused. valid values: (true,false)
            page : Page number of paginated results. default 1
            per_page : Number of firewall rules per page. default 25, min 5, max 100
        '''

        self.content = f"获取zone_id: {zone_id} 的firewall rules 列表"
        self.url_req = f"{self.url}/zones/{zone_id}/firewall/rules?page={page}&per_page={per_page}"
        self.method = "GET"
        self.verify = False
        self.data = {}

        if 'id' in dict_args:
            self.url_req += f"&id={dict_args['id']}"

        if 'description' in dict_args:
            self.url_req += f"&description={dict_args['description']}"
        
        if 'action' in dict_args:
            self.url_req += f"&action={dict_args['action']}"

        if 'paused' in dict_args:
            self.url_req += f"&paused={dict_args['paused']}"

        # srt = self._send_req()

        return self._send_req()

    def update_firewall_rules(self, zone_id, rules=[]):
        '''
            更新 zone_id 的firewall rules，可以一次性更新多条
            data: [
                {
                    'id': '238288a2f3c3499fbeb82fe30a07d094', ## Required
                    'paused': False, ## Optional parameters
                    'description': 'CC-03: www.alcp3.com', ## Optional parameters
                    'action': 'challenge', ## Optional parameters
                    'paused': False, ## Optional parameters
                    'filter': {'id': '347462a18d65410aa81e0d0cb15395a4', 'expression': 'http.host contains "alcp3.com" and http.request.uri contains "/login/login_ok?agname=" and (http.user_agent eq "Mozilla/4.0(compatible; MSIE 9.0; Windows NT 6.1)" or http.user_agent eq "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)" or http.user_agent eq "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)")'} ## Optional parameters
                },
                ]

            注意：利用此方法无法更新防火墙的规则表达式，即 expression。可利用当前class 的 update_firewall_rules_filters 来更新
        '''

        self.content = f"更新 zone_id: {zone_id} 的firewall rules"
        self.url_req = f"{self.url}/zones/{zone_id}/firewall/rules"
        self.method = "PUT"
        self.verify = False
        self.data = rules

        return self._send_req()

    def update_firewall_rules_filters(self, zone_id, filters=[]):
        '''
            更新 zone_id 的firewall rules 规则表达式
            data: [
                {
                    'id': '347462a18d65410aa81e0d0cb15395a4', ## Required
                    "id": data['data']['result'][0]['filter']['id'],
                    "paused": False,
                    "expression": 'http.host contains "alcp3.com" and http.request.uri contains "/login/login_ok?agname=" and http.user_agent eq "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"',
                    "description": "Restrict access from these browsers"
                },
                ]
        '''

        self.content = f"更新 zone_id: {zone_id} 的firewall rules 规则表达式"
        self.url_req = f"{self.url}/zones/{zone_id}/filters"
        self.method = "PUT"
        self.verify = False
        self.data = filters

        return self._send_req()

if __name__ == "__main__":
    print ("no more")