# daycount-NBT
MCDR插件，通过读取 NBT 文件，获取服务器总运行时间。

## 使用说明
简单的例子：
```python
from daycount import getday
def on_load(server, old):
  server.logger.info(getday())
```

## 配置插件
一般来说，你无需配置此插件，到手即用。如果您服务器的 `level.dat` 并非位于 `server/world/level.dat`，则需要手动配置。  
用任意编辑器打开 .py 文件，修改 `nbtPath` 即可。

## 重要说明
由于此插件原理是获取服务器世界时间，所以输出的 **并非** 开服时间，而是 **服务器总运行时长**。
