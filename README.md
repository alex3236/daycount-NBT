# daycount-NBT
MCDR插件，获取和输出服务器开服时间。

## 使用说明
### 安装前置
如果你只使用日期模式，则无需此前置。
```bash
pip install nbtlib
```

### API
简单的例子：
```python
from daycount import getday
def on_load(server, old):
  server.logger.info(getday())
```

## 配置插件
### NBT 模式
一般来说，你无需配置此插件，到手即用。如果您服务器的 `level.dat` 并非位于 `server/world/level.dat`，则需要手动配置。  
用任意编辑器打开 .py 文件，修改 `nbtPath` 即可。
```python
nbtFile = 'server/world/level.dat' # NBT位置
```
### 日期模式
修改硬编码，即可使用日期模式——这应该不需要解释。  
```python
dateMode = {
            'enable': False, # 是否启用日期模式
            'date':'2021-01-01' # 开服日期
            }
```

## NBT 模式说明
NBT 模式的原理是获取服务器世界运行时间，所以输出的 **并非** 开服时间，而是 **服务器总运行时长**。  
如果服务器回档，时间也会被还原到存档时的数值。  
实际上，这比开服时间更能表达服务器的有效开服时间（  
当然，使用日期模式可以避免这个问题。

## 已知问题
目前所有已知问题已修复。欢迎找茬~  
~~NBT模式下，服务器开服第一次 auto-save 前调用会报错~~

## 吐槽
点名批评友商 [DaycountR](https://github.com/Van-Nya/DayCountR)。  
作为一个“R”，将原本 [daycount](https://github.com/TISUnion/daycount) 的指令、代码逻辑完全打乱。  
莫名其妙将简单的功能写了六七十行，而我这个功能相差不大的插件才 46 行。
DaycountR 还使用了配置文件（只是实现日期加减，配置文件又何必要？就算强迫症，为何代码有六七十行之多？）  
作为一个简单的开服时间插件，坚守本分才是王道。
