import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MRBD64 import MR_morshed
 
        MR_morshed()
 
 
 
elif bit == "32bit":
 
        from MRBD32 import MR_morshed
 
 
        MR_morshed()
 
