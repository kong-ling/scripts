import os
import sys
import re

def list_pdf(dir):
    list_dirs = os.walk(dir)
    for root, dirs, files in list_dirs:
        for f in files:
            full_f = os.path.join(root, f)
            print(full_f)

list_pdf(r'C:\Users\lingkong\Documents\LingKong')
