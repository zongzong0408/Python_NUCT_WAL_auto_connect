import re
import subprocess

output = subprocess.check_output(["ipconfig"], universal_newlines=True)
gateway_match = re.search(r"預設閘道: ([\d.]+)*", output)

print(gateway_match)