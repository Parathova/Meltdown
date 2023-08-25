import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Meltdown",
    version="0.1",
    description="Woo climate change",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)