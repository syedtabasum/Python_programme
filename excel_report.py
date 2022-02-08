import pandas as pd
import xml.etree.ElementTree as ET 
import os
from pathlib import Path
import shutil

def excelsheet():
        cols = ["LOG", "DATE", "VERDICT"]
        rows = []

        tree = ET.parse('./tc_log.xml')
        root = tree.getroot()
        for e in root:
                name = e.find("LOG").text
                date = e.find("DATE").text
                status = e.find("VERDICT").text
                    
                rows.append({"name": name, 
                          "date": date,
                          "status": status})

        df = pd.DataFrame(rows, columns = cols) 
        df.to_csv('./xml_test.csv')

rootdir =r'.\SAMPLEWork'
string1="Final Verdict:INCONC"

for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        for file in os.listdir(d):
            if file=="tc_log.xml":
                path=d+"/"+file
                tree = ET.parse(path) 
                root = tree.getroot()
                for i in root.findall("TCASE"):
                    if i.findtext("VERDICT")!="PASS":
                        brr=i.findtext("LOG")
                        brr=brr.replace("\\","/")
                        drr=brr.split("/")
                        
                        dir_del=d+"\\"+drr[0]
                        root.remove(i)
                        shutil.rmtree(dir_del)
                        
                tree.write(path)
print("Process Completed")
excelsheet()              

