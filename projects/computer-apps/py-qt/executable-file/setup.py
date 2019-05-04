if sys.platform == "win32":
    base = "Win32GUI"
    PYQT5_DIR = "d:/programs/Python3/lib/site-packages/PyQt5"
    include_files = [
        "qml/",
        (os.path.join(PYQT5_DIR, "qml", "QtQuick.2"), "QtQuick.2"),
        (os.path.join(PYQT5_DIR, "qml", "QtQuick"), "QtQuick"),
        (os.path.join(PYQT5_DIR, "qml", "QtGraphicalEffects"), "QtGraphicalEffects"),
    ]

setup(
    name="exe",
    version="0.9",
    description="asd",
    author="Prosenjit Das",
    author_email="prosenjitearnkumar@gmail.com",
    options={"build_exe": {"includes": ["atexit",     "sip","PyQt5.QtCore","PyQt5.QtGui","PyQt5.QtWidgets",
                                    "PyQt5.QtNetwork","PyQt5.QtOpenGL", "PyQt5.QtQml", "PyQt5.QtQuick"],
                       "include_files": include_files,
                       "excludes" : ['Tkinter'],
                       # "optimize" : 2,
                       # "compressed" : True,
                       # "include_msvcr" : True,
                   }},
executables=[
    Executable(script="main.py",
               targetName="sample.exe",
               base=base)
]
)
