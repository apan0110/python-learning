import os

# specify the directory path you want to list
directory_path = input("Enter directory path (leave empty for current directory): ")

# if no path is provided, use current directory
if not directory_path:
    directory_path = "."

try:
    # list contents of the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except Exception as e:
    print("Error:", e)
