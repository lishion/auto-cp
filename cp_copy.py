import sys
import os
import json
file_name = ".cp-config" 
dir = os.path.realpath(sys.path[0])
if not os.path.exists(file_name):
    print("[!] config file not exist, please run cp-init")
try:
    with open(file_name) as json_file:
        data = json.load(json_file)
        keyword = "|".join(data["keywords"])
        pattern = f"^\S+?\.({keyword})$"
        url = data["url"]
        os.system(f"{dir}/auto-cp.sh '{pattern}' {url}")
except expression as identifier:
    print("[!] open config file faild, please run cp-init")
    pass
