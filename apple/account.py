#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json
import sys
import os
import time
import base64
import jwt
import gzip

from middleware.telegram import send_telegram
from middleware.supersign import SuperSign
from middleware.logger import logger
from config import super_signature, apple_url, remind_count, message

# 获取上级目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取当前脚本路径
cur_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 复制超级签接口数据
super_signature_d = super_signature.copy()

# 循环获取超级签账号信息
logger.info(f"\n"*5)
for customer in super_signature_d.keys():

    # 测试一些数据
    # if customer != "leying": continue

    # 记录错误数据
    super_signature_d[customer]['error'] = ""

    logger.info(f"#"*100)
    logger.info(f"开始操作 业主: {customer}")
    
    super_url = super_signature_d[customer]["url"]
    logger.info(f"超级签URL: {super_url}")

    # 获取超级签账号信息
    ss = SuperSign(super_url)
    data = ss.get_data()['data']

    if data:
        for acc in data:

            # 测试一些数据
            # if acc['account'] != "liaohe035huanya@163.com": continue

            # 苹果采用的 ES256 编码方式，key是需要分段(\n)的，密钥头尾的"—BEGIN PRIVATE KEY—"也是必须的。之前我一直直接复制privatekey以文本的形式输入，在HS256下正常但是ES256会报错ValueError: Could not deserialize key data。
            private_key = "-----BEGIN PRIVATE KEY-----" + acc['p8'].replace("-----BEGIN PRIVATE KEY-----", "").replace("-----END PRIVATE KEY-----", "").replace(" ", "\n") + "-----END PRIVATE KEY-----"

            logger.info(f"账号: {acc['account']}")
            # logger.info(f"账号信息: {acc}")

            # payload
            token_dict = {
                "exp": time.time() + 20*60,  # 时间戳, token 有效时间 20分钟
                "iss": acc['iss'],
                "aud": "appstoreconnect-v1"
            }

            # headers
            headers = {
                "alg": "ES256",  # 声明所使用的算法。
                "kid": acc['kid'],
                "typ": "JWT",
            }
            
            try:
                # 使用jwt 获取苹果开发者 接口token
                jwt_token = jwt.encode(token_dict, private_key, algorithm="ES256", headers=headers)
                token = str(jwt_token, encoding='utf-8')
                
                # 苹果开发者 接口 请求头
                app_headers = {"Authorization": f"Bearer {token}"}

            except Exception as e:
                logger.error(f"获取苹果开发者 接口token 错误: {str(e)}")

            else:
                # 测试苹果开发者接口，判断账号能否正常使用
                app_ret = None
                try:
                    ret = requests.get(apple_url, headers=app_headers, verify=False, timeout=15)
                    app_ret = ret.json()
                    if "errors" in app_ret.keys():
                        super_signature_d[customer]['error'] += f"{acc['account']}: {str(app_ret)}\n"
                except Exception as e:
                    app_ret = str(e)
                    super_signature_d[customer]['error'] += f"{acc['account']}: {app_ret}\n"
                logger.info(f"苹果接口返回信息: {app_ret}")

# logger.info(super_signature_d)

# 发送预警信息
for customer in super_signature_d.keys():
    if super_signature_d[customer]['error']:
        message['text'] = "\n".join([
            "认证出现错误: ",
            f"业主: {customer}",
            super_signature_d[customer]['error'],
        ])
        send_telegram(message)

