import xieos
import os
import xd.check as check_os
xieos.hello('config/config.json')
while True:
    main = input('>')
    # 插件管理器
    if main == 'plugins':
        v = check_os.ver_check('config/config.json')
        if v == 'pro':
            xieos.plugins_manager('config/config.json', 'plugins')
        else:
            print("\033[0;31;40m免费版无法使用插件功能，请购买序列号\033[0m")
    # 清理终端
    elif main == 'clear':
        os.system('cls')
    # 系统信息
    elif main == 'ls':
        xieos.hello_a('config/config.json')
    # 音乐播放器插件
    elif main == 'music-tools':
        os.system('plugins\music.exe')
    # 购买序列号
    elif main == 'buy-pro':
        os.system('buy-pro\go.exe')
    # 命令错误
    else:
        print("\033[0;31;40m命令错误(0)\033[0m")
