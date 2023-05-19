# daycount-NBT

[![](https://img.shields.io/badge/for-mcdr%202-9cf?style=for-the-badge)](https://github.com/Fallen-Breath/MCDReforged)

MCDR插件，获取和输出服务器开服时间。

## 🚪 前置

```python
mcdreforged>=2.2.0
```

## 📝 使用说明

### ⚙️ 命令与自定义

你可以自定义 daycount-NBT 的命令，及其输出的字符串。其默认配置如下。

```json
"commands": ["!!day", "!!days"],
"day_text": "这是服务器开服的第 {day} 天"
```

如你所见，在输出字符串中，请用 `{day}` 代表开服天数，使用 `{{` 和 `}}` 来描述单个 `{` 和 `}`。
### 📡 NBT 模式

**使用 NBT 模式需要额外安装前置模块 `nbtlib>=2.0.0`。**

daycount-NBT **默认即 NBT 模式**，一般无需进行任何配置，到手即用。

如果您服务器的 `level.dat` 并非位于 `server/world/level.dat`，则需配置文件中的 `nbt_file`。

```json
"nbt_file": "path/to/level.dat"
```

> ⚠️**注意**：NBT 模式的原理是获取服务器世界运行时长，所以输出的并非开服时长，而是地图的在线总时长。如果服务器回档，时间也会被还原到存档时的数值。实际上，这比开服时间更能表达服务器的有效游玩时间。

当然，使用日期模式可以避免这个问题。

### 📅 日期模式

修改配置文件，关闭 NBT 模式并设置日期，即可使用日期模式。

```json
"nbt_mode": false,
"start_date": "2022-01-01"
```

日期格式应为 `%Y-%m-%d`。

### 🏳️ API

如果你不是开发者，则无需了解这部分内容。

```python
from daycount_nbt import getday, get_day_text
# 更多导入插件相关信息请看
# https://mcdreforged.readthedocs.io/zh_CN/latest/plugin_dev/basic.html#import-a-plugin

getday()
    """获取该服务器自建立以来已经运行了多少天。

    返回值:
        `int`: 整数天数。如果发生错误则为 `-1`。
    """

get_day_text()
    """根据 `config.dat_text` 返回在 `config.command` 中设置的命令被执行时应该输出的内容。

    返回值:
        `str`: 上文提到的内容。
    """
```
