import re
import subprocess

output = subprocess.check_output(["ipconfig"], universal_newlines=True)
print(output)
gateway_match = re.search(r"Default Gateway.*: ([\d.]+)", output)
print(gateway_match)