import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("MRBD64").file()
except Exception as e:
    exit(str(e))


import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("MRBD32").file()
except Exception as e:
    exit(str(e))
