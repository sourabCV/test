import os
import sys

a = os.system("nohup python3 /home/pi/DS/test/hello.py &")
print(a)
sys.exit(0)
