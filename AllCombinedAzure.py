# importing os module  
import os 
  
# importing shutil module  
import shutil 
  
#Source path 
#source = "/home/User/Documents/file.txt"
  
# Destination path 
destination = "/ApplicationData/Essbase/Validation/ShipTo/ResultSets/AllCombinedUsingPythonScript.json"
filenames = [ #'C:/Users/purnima.yadav/Documents/PY/vALIDATIONS/UPload/ShipToBaseDiscrepancy.json',
             '#C:/Users/purnima.yadav/Documents/PY/vALIDATIONS/UPload/ShipToBaseDuplicates.json'
            '/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseDiscrepancy.json',
            '/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseDuplicates.json',
            '/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseOrphan.json'
     ]       

with open('AllCombinedUsingPythonScript.json', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
				