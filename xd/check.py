import json


# 检查是否存在正版序列号
def check_key(path):
    f = open(path, 'r', encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    # 免费版序列号
    if data['key'] == '101010101':
        print("\033[0;32;40m版本激活检查成功！\033[0m")
        print('\033[0;31;40m经检测，您的软件为未授权免费版,可使用“buy-pro”指令获取序列号\033[0m')
    # 付费版序列号
    if data['key'] == '20100728':
        print("\033[0;32;40m版本激活检查成功！\033[0m")
        print("\033[0;32;40m检测到已授权序列号\033[0m")


def ver_check(path):
    f = open(path, 'r', encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    if data['key'] == '20100728':
        result = 'pro'
        return result
    else:
        result = 'n'
        return result
