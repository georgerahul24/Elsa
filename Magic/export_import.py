import json
from tkinter import filedialog
from Magic import theme, indexer,tkinterlib
from .Elsa_logging import log


def export(mode = 'f') -> None | str:
    """This function is to export the data"""
    from os import getcwd
    # see https://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter
    with open(f'{getcwd()}/resources/ users.elsa') as usernamefile:  # Opening user file
        username_data = json.load(usernamefile)
    datadict = {"indexfolders": indexer.read_indexer_folders(), "theme": theme.read_theme(), "usernames": f"{username_data}"}

    if mode == 'f':  # i.e. package data to be written to a file
        if (f := filedialog.asksaveasfile(mode = "w", defaultextension = ".json")) is not None:
            try:
                json.dump(datadict, f, indent = 4)
                f.close()
                log.info("Successfully exported the data")

            except Exception as e: log.error("Some error happened while exporting data", e)
        else: print("No file selected")
    elif mode == 's': return json.dumps(datadict)  # i.e. package dta to be send to server


def import_data(dat: dict | bool = None) -> None:
    """This function is to import the data"""
    try:
        from os import getcwd, remove
        initpth, indexerpth = (getcwd() + "/resources/ initial.elsa"), (getcwd() + "/resources/ indexerpaths.elsa")
        flag = False
        if dat is None:
            if (f := filedialog.askopenfile(mode = "r", defaultextension = ".json")) is not None:
                data = json.load(f)
                flag = True
                f.close()
        else: data = dat;flag = True
        if flag:
            indexdata, themedata, usernamedata = data.get("indexfolders"), data.get("theme"), data.get("usernames")
            if indexdata is not None:
                with open(indexerpth, "w") as indexfile:
                    json.dump(indexdata, indexfile, indent = 4)
                try: remove((getcwd() + "/resources/ indexer.elsa"))  # To re-built the indexes
                except: pass
            with open(initpth, "w") as themefile:
                themefile.write(f"{themedata[0]};{themedata[1]};{themedata[2]}")
                # see https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
            # json doesn't allow single quotes. Only allows double qoutes
            usernamedata = json.loads(usernamedata.replace("'", '"'))
            with open((getcwd() + "/resources/ users.elsa"), "w") as userfile:
                json.dump(usernamedata, userfile, indent = 4)
            log.info("Imported usernames from server")
            tkinterlib.reset_colors()
            del initpth, indexerpth, data, indexdata, themedata, usernamedata
    except Exception as e: log.error("Some error happened", e)
