from distutils.core import setup
import py2exe

#setup(name='baibaoxiang',
#      version='1.0',
#      description='BaiBaoXiang is to assist your study',
#      author='Ling Jiahe(Class 2, Grade 6)',
#      py_module=['show_word.py']
#     )

setup(console=['show_word.py'])
#setup(windows=["show_word.py"], options={"py2exe":{"dll_excludes":["MSVCP90.dll"]}})
