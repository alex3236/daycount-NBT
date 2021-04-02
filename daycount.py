from mcdreforged.api.all import *
from datetime import datetime
from math import floor

nbtFile = 'server/world/level.dat'
dateMode = {
            'enable': False,
            'date':'2021-01-01'
            }

PLUGIN_METADATA = {
    'id': 'daycount_nbt',
    'version': '3.0',
    'name': 'DayCount-NBT',
    'description': '通过读取 NBT 文件，获取服务器总运行时间。',
    'author': 'Alex3236',
    'link': 'https://github.com/eagle3236'
}

def getday():
    try:
        global nbtFile, dateMode
        if dateMode['enable']:
            return (datetime.now() - datetime.strptime(dateMode['date'], '%Y-%m-%d')).days
        else:
            import nbtlib
            return floor(nbtlib.load(nbtFile)['']['Data']['Time'] / 1728000)
    except:
        return 0
        raise


def display_days(source: CommandSource):
    source.reply(f'PTC 的有效运行时间是 {getday()} 天')


def on_info(server, info: Info):
    if not info.is_user:
        if info.content == 'Saved the game':
            global game_saved
            game_saved = True


def on_load(server: ServerInterface, old):
    server.register_command(Literal('!!day').runs(display_days))
    server.register_help_message('!!day', '查看服务器运行天数')
