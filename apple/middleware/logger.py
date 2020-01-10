#!/usr/bin/env python3
#-_- coding: utf-8 -_-

import logging
import os

# 获取上级目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 记录日志
logging.basicConfig(level=logging.INFO, filename=f"{base_dir}/logs/ss.log", format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)