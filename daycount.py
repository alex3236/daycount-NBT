from mcdreforged.api.all import *
from datetime import datetime
from math import floor

# -----------------------------------------
nbt_file = 'server/world/level.dat' # NBT 文件位置，设置为 -1 以使用日期模式
start_date = '2021-01-01' # 开服日期
# -----------------------------------------

PLUGIN_METADATA = {
    'id': 'daycount_nbt',
    'version': '4.0',
    'name': 'DayCount-NBT',
    'description': '通过读取 NBT 文件，获取服务器总运行时间。',
    'author': 'Alex3236',
    'link': 'https://github.com/eagle3236'
}
 
def getday():
    try:
        global nbt_file, start_date
        if isinstance(nbt_file, str):
            import nbtlib
            return floor(nbtlib.load(nbt_file)['']['Data']['Time'] / 1728000)
        return (datetime.now() - datetime.strptime(start_date, '%Y-%m-%d')).days
    except Exception:
        return 0


def display_days(source: CommandSource):
    source.reply(f'这是服务器开服的第 {getday()} 天')


def on_load(server: ServerInterface, old):
    server.register_command(Literal('!!day').runs(display_days))
    server.register_help_message('!!day', '查看服务器运行天数')
