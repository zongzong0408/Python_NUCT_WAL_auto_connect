import os
import winreg

# Specify the directory to add to the user's PATH
directory_to_add = r'C:\your\directory\path'  # Replace this with the directory path you want to add

# Open the user's Environment registry key
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_ALL_ACCESS)

# Get the current user's PATH value
current_path_value, _ = winreg.QueryValueEx(key, 'PATH')

# Check if the directory is already in PATH
if directory_to_add not in current_path_value:
    # Append the directory to PATH
    new_path_value = f'{current_path_value};{directory_to_add}'

    # Set the updated PATH value in the registry
    winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path_value)

    print(f"Directory '{directory_to_add}' added to user's PATH variable.")
else:
    print(f"Directory '{directory_to_add}' already exists in user's PATH variable.")

# Close the registry key
winreg.CloseKey(key)

# Notify the system of the environment change
os.environ['PATH'] = new_path_value
