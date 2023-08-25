import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}

base = "Win32GUI" if sys.platform == "win32" else None

options = {
    'build_exe': {
        'include_files': {
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        }
    }
}

setup(
    name="Meltdown",
    version="0.1",
    description="Woo climate change",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)