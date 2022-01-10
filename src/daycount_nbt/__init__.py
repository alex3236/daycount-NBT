from mcdreforged.api.all import *
from datetime import datetime
from traceback import print_exc
from typing import List
import nbtlib


class Configure(Serializable):
    commands: List[str] = ['!!day', '!!days']
    nbt_mode: bool = True
    nbt_file: str = 'server/world/level.dat'
    start_date: str = '2022-01-01'
    day_text: str = '这是服务器开服的第 {day} 天'


config: Configure

def getday() -> int:
    """Get how many days the server has been running since its establishment.

    Returns:
        `int`: Integer number of days, or `-1` if an error occurs
    """
    try:
        if config.nbt_mode:
            return int(nbtlib.load(config.nbt_file)['Data']['Time'] / 1728000)
        return (datetime.now() - datetime.strptime(config.start_date, '%Y-%m-%d')).days
    except:
        print_exc()
        return -1


def get_day_text() -> str:
    """Returns the content which should be output when a command set in `config.commands` is executed, according to the `config.dat_text`.

    Returns:
        `str`: The content mentioned above.
    """
    return config.day_text.format(day=str(getday()))


def display_days(source: CommandSource):
    source.reply(get_day_text())


def on_load(server: PluginServerInterface, old):
    global config
    config = server.load_config_simple(target_class=Configure)
    if not config.commands: config.commands = config.get_default().commands 
    server.register_command(Literal(config.commands).runs(display_days))
    server.register_help_message(config.commands[0], '查看服务器运行天数')
    server.get_server_information()