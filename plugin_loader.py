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
    try:
        plugins = plugins.replace(".py", "")

        exec(f"from plugins import {plugins}") # Importing the plugin
        exec(f"""for  plugincmds in {plugins}.plugin_loader: # iterating through pluginloader variable
           pluginhandlerdict[plugincmds[0]]=plugincmds[1]""") # adding the keyword of the plugin and the func it calls to the dict
    except: pass
print("Finished Loading Plugins:", *pluginslist)
history.user_file("Loaded plugins", f"Following plugins were loaded: {pluginslist}")


def plugin_handler(keyword, afterword):
    pluginhandlerdict[keyword](f'{keyword} {afterword}')
    history.user_file(keyword + afterword, "Using plugins to resolve the query")
