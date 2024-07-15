# 插件管理器核心驱动
import json
def p_list(path):
    r = open(path,'r',encoding='utf-8')
    data = r.read()
    data = json.loads(data)
    plugin_list = data['plugins']
    print("\033[0;33;40m插件列表\033[0m")
    for i in plugin_list:
        print(i)
    print("\033[0;32;40m插件查询结束！\033[0m")

