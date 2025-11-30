from subprocess import run
from os import system

brillo = int(run(["ddcutil", "getvcp", "10"], capture_output=True, text=True).stdout[66:69])

if brillo > 10:
    system(f'ddcutil setvcp 10 {brillo - 10}')
elif brillo == 0:
    pass
else:
    system(f'ddcutil setvcp 10 0')
