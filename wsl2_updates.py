#!/usr/bin/python3

import os
import subprocess

# Update the environment variable
os.environ['VAGRANT_WSL_ENABLE_WINDOWS_ACCESS'] = 1

# Verify the updated value
print('VAGRANT_WSL_ENABLE_WINDOWS_ACCESS = ' + os.environ['VAGRANT_WSL_ENABLE_WINDOWS_ACCESS'])

# Add the VirtualBox path to the PATH environment variable
app_path = "/mnt/c/Program Files/Oracle/VirtualBox"
os.environ["PATH"] += os.pathsep + app_path

print ('Added VirtualBox path to PATH: ' + os.environ["PATH"])

# Run the shell command
process = subprocess.run('vagrant plugin install virtualbox_WSL2', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
print(process.stdout)