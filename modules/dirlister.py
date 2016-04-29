__author__ = 'leale'
import os
def run(**args):
    print"[*] loading dir moulde"
    files = os.listdir(".")
    return  str(files)
