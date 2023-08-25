import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("YOUR_PROGRAM.py", base=base, targetName="NAME_OF_EXE")]

cx_Freeze.setup(
    name="NAME_OF_EXE",
    options={"build_exe": {"packages": ["tkinter"], "include_files": [
        "someImage.png", "anotherImage.png",
    ]}},
    version="1.0",
    description="DESCRIBE YOUR PROGRAM",
    executables=executables
)