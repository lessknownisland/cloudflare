#!/usr/bin/env python3
#-_- coding: utf-8 -_-
import platform

cf_accounts = {}

timeout = 5

manage = {
    'ali': {
        'email': "alialicp66@gmail.com",
        'key': "bc4a4aa5751ce4e49f14cc1b5bbc9e34ff76c",
        'zone_id': "3bee46089f8144e942688b3954fdc484",
        'zone': "alcp08.com",
        'record': "manage.alcp08.com",
        'whitelist': [''],
    },
    'uc': {
        'email': "lebo.technical001@gmail.com",
        'key': "be7a47dea417a6e2ecefacedce5908b292f5a",
        'zone_id': "24b71fdaab8f4a6b6ba576e50eb1779c",
        'zone': "uc222.co",
        'record': "manage.uc222.co",
        'whitelist': ['110.54.147.228'],
    },
    'gd': {
        'email': "guangdagdcp@gmail.com",
        'key': "78ae89a46c08fc9ae8833f0bc542c525d7dfb",
        'zone_id': "25febaeb5c788cdf1c8ab79e71b379a7",
        'zone': "gdcp158.com",
        'record': "manage.gdcp158.com",
        'whitelist': [''],
    },
    'hengda': {
        'email': "hengda668@gmail.com",
        'key': "51d1510b91ea02e75729c18c9c5f3cb68f124",
        'zone_id': "94fcce25ac0c98668537422753c93c95",
        'zone': "hdcp018.com",
        'record': "manage.hdcp018.com",
        'whitelist': [''],
    },
    'ct': {
        'email': "lebo.technical001@gmail.com",
        'key': "be7a47dea417a6e2ecefacedce5908b292f5a",
        'zone_id': "dc6213e7c10f81484dd859c38e262bff",
        'zone': "caitou999.com",
        'record': "manage.caitou999.com",
        'whitelist': [''],
    },
    'sd': {
        'email': "richer668668@gmail.com",
        'key': "912bf351941d93e14e29bf79a50eef1d50cc5",
        'zone_id': "5d92f0bc9749f7fc90e627d528607115",
        'zone': "208608.com",
        'record': "manage.208608.com",
        'whitelist': [''],
    },
    'leying': {
        'email': "lycplycp1212@outlook.com",
        'key': "7174c702d57d7ff2572cce0931758855dbb6c",
        'zone_id': "238be2d76f13b2046d08b3c173344939",
        'zone': "le064.com",
        'record': "manage.le064.com",
        'whitelist': ['116.93.44.56'],
    },
    'agcai': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "6a3cc0a2593ba5774f8c5268f6bbef51",
        'zone': "ag99999.cc",
        'record': "manage.ag99999.cc",
        'whitelist': ['211.72.15.15'],
    },
    'yiteng': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "772e821f37a4317e67a077c5c22fad5e",
        'zone': "et533.com",
        'record': "manage.et533.com",
        'whitelist': [''],
    },
    'feixin': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "4916380bcae50f58e98642fa6fd7c66a",
        'zone': "fx5533.com",
        'record': "manage.fx5533.com",
        'whitelist': [''],
    },
    '567bet': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "5d8c678e2bafa1012013b13f6a1b0f75",
        'zone': "2222789.com",
        'record': "manage.2222789.com",
        'whitelist': [''],
    },

    #体彩
    'ubs': {
        'email': "le1.tech001@gmail.com",
        'key': "29697a07614e03226eb4d32e08b0c2e337cf2",
        'zone_id': "ff1b16dfe0db17c3d36fd0b73dbf0279",
        'zone': "6686cp.com",
        'record': "manage.6686cp.com",
        'whitelist': ['111.125.91.79','111.125.91.80','111.125.91.81','111.125.91.82','116.93.65.175','116.93.65.176','116.93.65.177','116.93.65.178','122.55.212.220','122.55.212.221','122.55.212.222'],
    },
    'warrior': {
        'email': "xiaoxuanzi120@gmail.com",
        'key': "c105c007dca8e66533b68875a3311b8dd56bc",
        'zone_id': "21417c5997a75140ca67887d2c1abce9",
        'zone': "8868hgcp.com",
        'record': "manage.8868hgcp.com",
        'whitelist': ['111.125.91.79','111.125.91.80','111.125.91.81','111.125.91.82','116.93.65.175','116.93.65.176','116.93.65.177','116.93.65.178','122.55.212.220','122.55.212.221','122.55.212.222'],
    },
    'ldc': {
        'email': "xiaoxuanzi120001@gmail.com",
        'key': "af7231e4263c5a73c4038d21d084e51485573",
        'zone_id': "f27907bbc6d408730a65d60839571536",
        'zone': "ldccp999.com",
        'record': "manage.ldccp999.com",
        'whitelist': ['111.125.91.79','111.125.91.80','111.125.91.81','111.125.91.82','116.93.65.175','116.93.65.176','116.93.65.177','116.93.65.178','122.55.212.220','122.55.212.221','122.55.212.222'],
    },
    'diamond': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "92d634000c1d3e2726f82060680931d1",
        'zone': "338caip.com",
        'record': "manage.338caip.com",
        'whitelist': [''],
    },
    '188cp': { #3535
        'email': "lebo.technical001@gmail.com",
        'key': "be7a47dea417a6e2ecefacedce5908b292f5a",
        'zone_id': "23b4322c93997f583ef2f1533309a194",
        'zone': "mcp3535.com",
        'record': "manage.mcp3535.com",
        'whitelist': [''],
    },
    '9393cp': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "4d718a2a96fb7525c2607e6e1418cd33",
        'zone': "cp9393.co",
        'record': "manage.cp9393.co",
        'whitelist': [''],
    },
    '1717cp': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "8722ac13b44e2d3cabfdfc79c7e4a73c",
        'zone': "cp1717.cc",
        'record': "manage.cp1717.cc",
        'whitelist': [''],
    },
    'bcsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "96b7b871132d9be110acd6b4c31a803a",
        'zone': "sup-bccccp.com",
        'record': "manage.sup-bccccp.com",
        'whitelist': ['112.211.73.184', '23.247.69.67', '113.10.160.25', '58.64.187.22', '58.64.187.20', '113.10.160.29', '104.223.178.3', '104.223.172.3', '103.70.187.3', '103.70.185.3', '23.247.95.3', '23.247.120.3', '107.179.17.3', '104.223.236.3', '103.115.205.115', '103.115.205.107', '103.115.205.99', '103.115.205.91', '103.115.205.147', '103.115.205.139'],
    },
    'vgsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "5b2afea35a1891dea2a6fe29aa8fe1ce",
        'zone': "bananatwo.site",
        'record': "admin-lottery-stg.bananatwo.site",
        'whitelist': ['60.248.107.94','60.248.107.95','60.248.107.96','60.248.107.166','60.248.107.167','60.248.107.168','124.12.176.240','124.12.176.241','124.12.176.242','124.12.176.243','124.12.176.244','124.12.176.245','124.12.176.246','124.12.176.247','18.140.161.24','18.140.112.134','18.140.126.56','18.176.208.30','18.176.223.49','18.176.230.46'],
    },
    'xmsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "d7eca9a5ab7c02534e71c2ff19a39816",
        'zone': "winxmcp.com",
        'record': "xmty.winxmcp.com",
        'whitelist': ['116.93.44.59', '116.93.30.11', '116.50.189.11', '118.143.201.169', '116.93.38.27'],
    },
    'apiopen': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "781c3a80acd9071bf71855813dc37833",
        'zone': "apitotal.com",
        'record': "l5jiamei.apitotal.com",
        'whitelist': ['13.209.174.65', '13.124.40.142', '13.125.153.96'],
    },
    'bet365sport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "2c4721b629cf8176ebe218554f1f2725",
        'zone': "babet365.com",
        'record': "tycpmanage.babet365.com",
        'whitelist': ['103.108.43.116','103.108.43.117','103.108.43.118','103.108.43.119','103.108.43.120','103.108.43.121','103.108.43.113','103.108.43.114','103.108.43.115','103.108.43.110','103.108.43.111','103.108.43.112','103.108.41.71','103.108.41.72','103.108.41.73','103.108.41.41','103.108.41.42','103.108.41.43','58.177.186.8'],
    },
    'ffsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "2916f7c6dad7547d07d3d1d2af32ac47",
        'zone': "fftylt.com",
        'record': "fftyht.fftylt.com",
        'whitelist': ['52.78.101.41'],
    },

    'ali-al885.com': {
        'email': "alcpalcp1212@outlook.com",
        'key': "bc4a4aa5751ce4e49f14cc1b5bbc9e34ff76c",
        'zone_id': "9a32c1b82d6886586b4be5f656d0b1b6",
        'zone': "al885.com",
        'record': "www.al885.com",
        'whitelist': ['180.124.24.202'],
    },

}

if __name__ == '__main__':
    print (platform.python_version())
    print ("%s is just a config file." %__file__)
