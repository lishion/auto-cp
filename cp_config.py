import sys
import os
import getopt
import json
keywords = ""
url = ""
opts,args = getopt.getopt(sys.argv[1:],"k:u:")
for op,value in opts:
    if op=="-k":
        keywords = value
    elif op=="-u":
        url = value

data = {"keywords":keywords.split(","),"url":url}
shell_path = os.getcwd()
try:
    with open(".cp-config","w") as config:
         json.dump(data,config,ensure_ascii=False)
except BaseException as e:
    print("init false")
    print(e.message)
print("[*] init success")
print(f"[*] files with postfix in [ {keywords} ] will copy to {url}")

        