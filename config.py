#!/usr/bin/env python3
#-_- coding: utf-8 -_-
import platform

cf_accounts = {}

timeout = 5

manage = {
    'ali': {
        'email': "alcpalcp1212@outlook.com",
        'key': "bc4a4aa5751ce4e49f14cc1b5bbc9e34ff76c",
        'zone_id': "3bee46089f8144e942688b3954fdc484",
        'zone': "alcp08.com",
        'record': "manage.alcp08.com",
        'whitelist': ['110.54.210.70'],
    },
    'alcp3.com': {
        'email': "alcpalcp1212@outlook.com",
        'key': "bc4a4aa5751ce4e49f14cc1b5bbc9e34ff76c",
        'zone_id': "00fa96d8db427fdd9fbdc9865952a571",
        'zone': "alcp3.com",
        'record': "alcp3.com",
        'whitelist': ['1.197.244.0/24', '1.197.245.0/24'],
    },
    'uc': {
        'email': "lebo.technical001@gmail.com",
        'key': "be7a47dea417a6e2ecefacedce5908b292f5a",
        'zone_id': "24b71fdaab8f4a6b6ba576e50eb1779c",
        'zone': "uc222.co",
        'record': "manage.uc222.co",
        'whitelist': ['175.176.32.71'],
    },
    'gd': {
        'email': "gdcpgdcp1212@outlook.com",
        'key': "78ae89a46c08fc9ae8833f0bc542c525d7dfb",
        'zone_id': "25febaeb5c788cdf1c8ab79e71b379a7",
        'zone': "gdcp158.com",
        'record': "manage.gdcp158.com",
        'whitelist': ['110.54.210.70'],
    },
    'venetian': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "4eed0d216d4afac769d851af5865db26",
        'zone': "manage5765.com",
        'record': "cp.manage5765.com",
        'whitelist': ['110.54.210.70'],
    },
    # 'hengda': {
    #     'email': "hengda668@gmail.com",
    #     'key': "51d1510b91ea02e75729c18c9c5f3cb68f124",
    #     'zone_id': "94fcce25ac0c98668537422753c93c95",
    #     'zone': "hdcp018.com",
    #     'record': "manage.hdcp018.com",
    #     'whitelist': [''],
    # },
    'ct': {
        'email': "lebo.technical001@gmail.com",
        'key': "be7a47dea417a6e2ecefacedce5908b292f5a",
        'zone_id': "dc6213e7c10f81484dd859c38e262bff",
        'zone': "caitou999.com",
        'record': "manage.caitou999.com",
        'whitelist': ['180.191.159.150'],
    },
    'sd': {
        'email': "sdcpsdcp1212@outlook.com",
        'key': "912bf351941d93e14e29bf79a50eef1d50cc5",
        'zone_id': "5d92f0bc9749f7fc90e627d528607115",
        'zone': "208608.com",
        'record': "manage.208608.com",
        'whitelist': ['110.54.152.165'],
    },
    'sd2': {
        'email': "sdcpsdcp1212@outlook.com",
        'key': "912bf351941d93e14e29bf79a50eef1d50cc5",
        'zone_id': "984214f00b256df58937a079ddfcc524",
        'zone': "668cp.cc",
        'record': "manage.668cp.cc",
        'whitelist': ['111.125.91.78'],
    },
    'leying': {
        'email': "lycplycp1212@outlook.com",
        'key': "7174c702d57d7ff2572cce0931758855dbb6c",
        'zone_id': "238be2d76f13b2046d08b3c173344939",
        'zone': "le064.com",
        'record': "manage.le064.com",
        'whitelist': ['180.190.114.34'],
    },

    #体彩
    'ubs': {
        'email': "le1.tech001@gmail.com",
        'key': "29697a07614e03226eb4d32e08b0c2e337cf2",
        'zone_id': "ff1b16dfe0db17c3d36fd0b73dbf0279",
        'zone': "6686cp.com",
        'record': "manage.6686cp.com",
        'whitelist': ['110.54.161.77'],
    },
    'warrior': {
        'email': "xiaoxuanzi120@gmail.com",
        'key': "c105c007dca8e66533b68875a3311b8dd56bc",
        'zone_id': "21417c5997a75140ca67887d2c1abce9",
        'zone': "8868hgcp.com",
        'record': "manage.8868hgcp.com",
        'whitelist': ['110.54.245.79'],
    },
    'ldc': {
        'email': "xiaoxuanzi120001@gmail.com",
        'key': "af7231e4263c5a73c4038d21d084e51485573",
        'zone_id': "f27907bbc6d408730a65d60839571536",
        'zone': "ldccp999.com",
        'record': "manage.ldccp999.com",
        'whitelist': ['110.54.243.10'],
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
    'newregal': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "7ee31691f1980b50a88a6439c37376f4",
        'zone': "4927cpht.com",
        'record': "manage.4927cpht.com",
        'whitelist': ['103.71.237.164','103.71.237.170','103.71.237.173','112.206.107.147'],
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
        'whitelist': [''],
    },
    'vgsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "5b2afea35a1891dea2a6fe29aa8fe1ce",
        'zone': "bananatwo.site",
        'record': "admin-lottery-stg.bananatwo.site",
        'whitelist': [''],
    },
    'xmsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "d7eca9a5ab7c02534e71c2ff19a39816",
        'zone': "winxmcp.com",
        'record': "xmty.winxmcp.com",
        'whitelist': [''],
    },
    'apiopen': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "781c3a80acd9071bf71855813dc37833",
        'zone': "apitotal.com",
        'record': "l5jiamei.apitotal.com",
        'whitelist': ['180.191.159.194'],
    },
    # 'bet365sport': {
    #     'email': "L5yirencp@gmail.com",
    #     'key': "5321b5c5022b60107a9e5ad295539c58ee551",
    #     'zone_id': "2c4721b629cf8176ebe218554f1f2725",
    #     'zone': "babet365.com",
    #     'record': "tycpmanage.babet365.com",
    #     'whitelist': [''],
    # },
    'ffsport': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "2916f7c6dad7547d07d3d1d2af32ac47",
        'zone': "fftylt.com",
        'record': "fftyht.fftylt.com",
        'whitelist': ['52.78.101.41'],
    },
    'calculate': {
        'email': "L5yirencp@gmail.com",
        'key': "5321b5c5022b60107a9e5ad295539c58ee551",
        'zone_id': "f8887000822581cda1793f78de498e60",
        'zone': "calculate-lab.com",
        'record': "www.calculate-lab.com",
        'whitelist': ['180.191.159.194', '180.190.112.251'],
    },

    # 'ali-al885.com': {
    #     'email': "alcpalcp1212@outlook.com",
    #     'key': "bc4a4aa5751ce4e49f14cc1b5bbc9e34ff76c",
    #     'zone_id': "9a32c1b82d6886586b4be5f656d0b1b6",
    #     'zone': "al885.com",
    #     'record': "www.al885.com",
    #     'whitelist': ['180.124.24.202'],
    # },

}

if __name__ == '__main__':
    print (platform.python_version())
    print ("%s is just a config file." %__file__)
