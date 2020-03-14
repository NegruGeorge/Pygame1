import cx_Freeze
from cx_Freeze import *

setup(
    name = "app",
    options = {'build_exe':{'packages': ['pygame']}},
    executables=[
        Executable(
            "app.py",


            )




        ]


    )
