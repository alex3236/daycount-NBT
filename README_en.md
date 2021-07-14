[中文](README.md) | **English**
# daycount-NBT
MCDR plugin to get and export server opening times.

## Install Preceding
If you only use date mode, you don't need a pre-installation.
```bash
pip install nbtlib
```
## Instructions for use
### Command
`!!day`: Show the number of days the server has been open.

### API
If you are not a developer, you do not need to know this part.
Simple example.
```python
from daycount import getday
def on_load(server, old):
  server.logger.info(getday())
```
`getday()` will return an integer representing the number of days the server has been open.

## Configure the plugin
### NBT mode
In general, there is no configuration required to use NBT mode, it is ready to use right out of the box. If your server's `level.dat` is not located in `server/world/level.dat`, you will need to configure it manually.  
Open the .py file with any editor and modify `nbt_file`.
```python
nbt_file = 'server/world/level.dat' # NBT file location
```
**Note**: The principle of NBT mode is to get the server world runtime, so the output **is not the **opening time**, but the **total online time of the Minecraft server**.  
If the server is back archived, the time is also restored to the value at the time of archiving.  
In fact, this is a better representation of the server's effective start time than the start time (  
Of course, this problem can be avoided by using the date mode.

### Date mode
Modify the hardcoding to turn off NBT mode and set the date to use date mode.  
The date format should be `%Y-%m-%d`.'
