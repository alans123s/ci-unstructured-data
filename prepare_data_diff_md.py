import os
import pandas as pd
import json


with open('diff.json') as json_data:
    data = json.load(json_data)

list_add = [x for x in data['added'] if 'jpg' in x['path']]
list_mod = [x for x in data['modified'] if 'jpg' in x['path']]
list_del = [x for x in data['deleted'] if 'jpg' in x['path']]

os.system("touch report_mod.md report_add.md report_del.md")

if list_add:
    print(f"ADDED :{len(list_add)}")
    with open("report_add.md","w+") as f:
            pd.DataFrame(list_add).to_markdown(f)
    with open("report_add.md","r+") as f:
            content = f.read()
            f.seek(0,0)
            f.write("\r\n## ADDED FILES\n"+content)

if list_mod:
    print(f"mod :{len(list_mod)}")
    with open("report_mod.md","a+") as f: 
            online = f.readlines()
            online.insert(0,f"{pd.DataFrame(list_mod).to_markdown(f)}\n")
    with open("report.md","w") as f:
        f.writelines(online) 

    with open("report.md","r") as f:
            online = f.readlines()
            online.insert(0,"## MODIFIED FILES\n")
    with open("report.md","w") as f:
            f.writelines(online)  
if list_del:
    print(f"del :{len(list_del)}")
    with open("report_del.md","w+") as f:
            pd.DataFrame(list_del).to_markdown(f)
    with open("report_del.md","r+") as f:
            content = f.read()
            f.seek(0,0)
            f.write("\r\n## delED FILES\n"+content)
if not list_add and list_del and list_mod:
    with open("report.md","w") as f:
        f.write("## NO DATA CHANGES COMPARED TO MASTER")

filenames = ['report_add.md','report_mod.md','report_del.md']

with open("report.md","w") as outfile:
    for files in filenames:
        with open(files) as infile:
            outfile.write(infile.read())
        outfile.write("\n")
