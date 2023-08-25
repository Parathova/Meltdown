import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base = base, icon = "icon.png", targetName = "meltdown")]

cx_Freeze.setup(
    name = "meltdown",
    options = {"build_exe": {"packages": ["tkinter"], "include_files": [
        "background_img.png", "icon.png", "news.png", "pol_bar.png", "tab1.png",
        "tab2.png", "tab3.png", "tab4.png", "water_1.png", "water_p_1.png", "world.png",
    ]}},
    version = "1.0",
    description = "Woo climate change",
    executables = executables
)