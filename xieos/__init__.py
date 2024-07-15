import json
import time
import webbrowser

import xd.loading as loading_os
import xd.check as check_os
import xd.plugin as plugin_os
# 系统初始化UI
def hello(path):
    f = open(path,'r',encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    print("\033[0;33;40m系统信息\033[0m")
    time.sleep(1)
    print('名称',data['name'])
    time.sleep(1)
    print('版本号:',data['version'])
    time.sleep(1)
    print('本地序列号',data['key'])
    time.sleep(1)
    loading_os.loading('检查系统序列号','blue')
    check_os.check_key(path)
# 系统信息展示UI
def hello_a(path):
    f = open(path,'r',encoding='utf-8')
    data = f.read()
    data = json.loads(data)
    print("\033[0;33;40m系统信息\033[0m")
    time.sleep(1)
    print('名称',data['name'])
    time.sleep(1)
    print('版本号:',data['version'])
    time.sleep(1)
    print('本地序列号',data['key'])
# 插件管理器UI
def plugins_manager(path,plugins_path):
    loading_os.loading('插件查询中','green')
    plugin_os.p_list(path)
# 购买付费序列号UI
def buy_pro(pro):
    webbrowser.open(pro)

