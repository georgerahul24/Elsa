import os
import shutil
from Magic import history

try:
    # __pycache__ causing some problems...so deleting it every time it starts...
    shutil.rmtree(os.path.join(os.path.dirname(__file__), "plugins", "__pycache__"))
except: pass
print("Starting to load the plugins...")
pluginslist = os.listdir(os.path.join(os.path.dirname(__file__), "plugins"))
pluginhandlerdict = {}

for plugins in pluginslist:
    plugins = plugins.replace(".py", "")

    exec(f"from plugins import {plugins}")
    exec(f"""for  plugincmds in {plugins}.plugin_loader:
       pluginhandlerdict[plugincmds[0]]=plugincmds[1]""")

print("Finished Loading Plugins")


def plugin_handler(keyword, afterword):
    pluginhandlerdict[keyword](afterword)
    history.user_file(keyword + afterword, "Using plugins to resolve the query")
