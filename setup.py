# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('main.py', targetName='Kiber-Krolik.exe')]

includes = ['matplotlib', 'numpy', 'pytest', 'PyQt5', 'tkinter']

options = {
      'build_exe': {
            'includes': includes,
            'build_exe': 'build_windows'
      }
}
setup(name='KK-KiberKrolik',
      version='0.0.4',
      description='Farm accounting',
      executables=executables)
