import re
import subprocess

output = subprocess.check_output(["ipconfig", "/all"], universal_newlines=True)
gateway_match = re.search(r"Default Gateway.*: ([\d.]+)", output)