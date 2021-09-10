from mcdreforged.api.all import *
from datetime import datetime
from traceback import print_exc
from math import floor

class Configure(Serializable):
    nbt_mode: bool = True
    nbt_file: str = 'server/world/level.dat'
    start_date: str = '2021-01-01'
    day_text: str = '这是服务器开服的第 $day 天'

config: Configure
 
def getday():
    try:
        if config.nbt_mode:
            import nbtlib
            return floor(nbtlib.load(config.nbt_file)['']['Data']['Time'] / 1728000)
        return (datetime.now() - datetime.strptime(config.start_date, '%Y-%m-%d')).days
    except Exception:
        print_exc()
        return -1

def get_day_text():
    return config.day_text.replace('$day', str(getday()))

def display_days(source: CommandSource):
    source.reply(get_day_text())

def on_load(server: PluginServerInterface, old):
    global config
    config = server.load_config_simple(target_class=Configure)
    server.register_command(Literal('!!day').runs(display_days))
    server.register_help_message('!!day', '查看服务器运行天数')
