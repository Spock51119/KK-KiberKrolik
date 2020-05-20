import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
                                                      'bz2', 'select'], "includes": ['sqlite3', "PyQt5", "datetime"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "KiberKrolik",
        version = "0.1",
        description = "Farm accounting",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])