import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "meltdown",
    
    version = "1.0",
    description = "Woo climate change",
    executables = executables
)