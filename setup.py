import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
    'include_files':['tcl86t.dll', 'tk86t.dll', 'background_img.png', 'icon.png', 'news.png', 'pol_bar,png',
                     'tab1.png', 'tab2.png', 'tab3.png', 'tab4.png', 'water_1.png', 'water_p_1.png', 'world.png',
                     'buy.png', 'exp_con.png', 'exp_glo.png', 'exp_nat.png', 'exp_prov.png', 'lock.png']
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