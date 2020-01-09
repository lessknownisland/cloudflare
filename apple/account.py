#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys
import os
import time
import base64
import jwt

# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 获取当前目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 苹果账号
account = "juandizhilao749@163.com"
issure_id = "adfbf4f6-08f5-484d-a92c-29b321ba7a92"
key_id = "9365AKSB6X"
p8_file = f"{base_dir}/apple/p8/AuthKey_9365AKSB6X.p8"

# account = "gu1966318@126.com"
# issure_id = "09d26945-1a89-4f91-99ee-6bd1a3a9dadd"
# key_id = "MNB4626N93"
# p8_file = f"{base_dir}/apple/p8/AuthKey_MNB4626N93.p8"

private_key = ""

# payload
token_dict = {
    "exp": time.time() + 20*60,  # 时间戳
    "iss": issure_id,
    "aud": "appstoreconnect-v1"
}

# headers
headers = {
    "alg": "ES256",  # 声明所使用的算法
    "kid": key_id,
    "typ": "JWT",
}

private_key = open(p8_file, 'r').read()

jwt_token = jwt.encode(token_dict, private_key, algorithm="ES256", headers=headers)

url = "https://api.appstoreconnect.apple.com/v1/apps"

token = str(jwt_token, encoding='utf-8')

print (f"token: {token} \n")

app_headers = {"Authorization": f"Bearer {token}"}

ret = requests.get(url, headers=app_headers, verify=False, timeout=5)

print (ret.content)
