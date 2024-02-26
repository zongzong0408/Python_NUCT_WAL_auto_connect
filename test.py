import re
import subprocess

def get_default_gateway():
    try:
        ipconfig_result = subprocess.check_output(['ipconfig'], stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        # Splitting the output by lines
        ipconfig_lines = ipconfig_result.split('\n')
        # Finding the line containing the default gateway
        for line in ipconfig_lines:
            if 'Default Gateway' in line:
                # Extracting the default gateway IP address
                default_gateway = line.split(':')[-1].strip()
                return default_gateway
    except subprocess.CalledProcessError as e:
        print("Error executing ipconfig:", e.output)

# Get and print the default gateway
default_gateway = get_default_gateway()
if default_gateway:
    print("Default gateway:", default_gateway)
else:
    print("Default gateway not found.")