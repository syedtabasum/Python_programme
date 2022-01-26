# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:19:41 2022

@author: sytabasu
"""
import xml.etree.ElementTree as ET 
import os
from pathlib import Path
import shutil

rootdir =r'C:\Users\sytabasu\Desktop\SAMPLE WORK\SAMPLEWork'
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
                
