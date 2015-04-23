import subprocess
from subprocess import Popen, PIPE
import os

sudoPassword = '19!jobs!76'
command = 'sudo apt-get install apache2'
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))