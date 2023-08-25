import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("C:\Users\michaelliu\Documents\GitHub\Meltdown\main.py")]

cx_Freeze.setup(
    name = "meltdown",
    
    version = "1.0",
    description = "Woo climate change",
    executables = executables
)