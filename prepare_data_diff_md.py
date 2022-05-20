import os
import pandas as pd
import json

os.system('dvc diff --show-json master >> diff.json')

with open('diff.json') as json_data:
    data = json.load(json_data)

list_add = [x for x in data['added'] if 'jpg' in x['path']]
list_mod = [x for x in data['modified'] if 'jpg' in x['path']]
list_del = [x for x in data['deleted'] if 'jpg' in x['path']]

if list_add:
    with open("teste.md",'w') as f:
        pd.DataFrame(list_del).to_markdown(f)
    with open("teste.md",'r') as f:
            online = f.readlines()
            online.insert(0,'## ADDED FILES\n')
    with open("teste.md",'w') as f:
            f.writelines(online)  
elif list_mod:
    with open("teste.md",'w') as f:
        pd.DataFrame(list_del).to_markdown(f)
    with open("teste.md",'r') as f:
            online = f.readlines()
            online.insert(0,'## MODIFIED FILES\n')
    with open("teste.md",'w') as f:
            f.writelines(online)  
elif list_del:
    with open("teste.md",'w') as f:
        pd.DataFrame(list_del).to_markdown(f)
    with open("teste.md",'r') as f:
            online = f.readlines()
            online.insert(0,'## DELETED FILES\n')
    with open("teste.md",'w') as f:
            f.writelines(online)  