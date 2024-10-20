#!usr/bin/env python3
import subprocess

oops = subprocess.check_call(['ls', '-l'])
print(oops)
if not oops:
    subprocess.run(['echo', 'wait im goated'])