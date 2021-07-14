from mcdreforged.api.all import *
from datetime import datetime
from traceback import print_exc
from math import floor

# -----------------------------------------
nbt_mode = True # 是否使用 NBT 模式
nbt_file = 'server/world/level.dat' # NBT 文件位置
start_date = '2021-01-01' # 开服日期
day_text = '这是服务器开服的第 $day 天' # 显示文字
# -----------------------------------------

PLUGIN_METADATA = {
    'id': 'daycount_nbt',
    'version': '1.2.1',
    'name': 'DayCount-NBT',
    'description': '通过读取 NBT 文件，获取服务器总运行时间。',
    'author': 'Alex3236',
    'link': 'https://github.com/eagle3236'
}
 
def getday():
    try:
        if nbt_mode:
            import nbtlib
            return floor(nbtlib.load(nbt_file)['']['Data']['Time'] / 1728000)
        return (datetime.now() - datetime.strptime(start_date, '%Y-%m-%d')).days
    except Exception:
        print_exc()
        return -1

def get_day_text():
    return day_text.replace('$day', str(getday()))

def display_days(source: CommandSource):
    source.reply(get_day_text())

def on_load(server: ServerInterface, old):
    server.register_command(Literal('!!day').runs(display_days))
    server.register_help_message('!!day', '查看服务器运行天数')
