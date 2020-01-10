#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import requests
import json

from middleware.logger import logger

#telegram 通知
def send_telegram(message):
    try:
        ret = requests.post('http://sa.l510881.com/detect/send_telegram', data=json.dumps(message))
    except Exception as e:
        logger.error(str(e))