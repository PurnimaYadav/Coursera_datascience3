val clientId = "214fbea2-a1e6-45c2-8137-d99f5194bcc4"
val directoryId = "70e69b8e-af22-402c-a6f5-2f677c60b09d"
val dataLakeURL = "adl://biotechnecommondevadls.azuredatalakestore.net/"
val dataLakeDirectory = "ApplicationData/"
val dataLakeFile = "small_radio_json.json"
val mountName = "DevDLGood/"

spark.conf.set("fs.adl.oauth2.access.token.provider.type", "ClientCredential")
spark.conf.set("dfs.adls.oauth2.access.token.provider", "org.apache.hadoop.fs.adls.oauth2.ConfCredentialBasedAccessTokenProvider") 
#This sets Hadoop provider
spark.conf.set("fs.adl.oauth2.client.id", clientId)
spark.conf.set("fs.adl.oauth2.credential", dbutils.secrets.get(scope = "AeroDev-KeyVault", key = "CommonDevADLConnector"))
spark.conf.set("fs.adl.oauth2.refresh.url", "https://login.microsoftonline.com/" + directoryId + "/oauth2/token")

 

#Below setsup the Hadoop configuration, which is necessary for RDD related functionality used to pull the data
spark.sparkContext.hadoopConfiguration.set("dfs.adls.oauth2.access.token.provider.type", spark.conf.get("fs.adl.oauth2.access.token.provider.type"))
spark.sparkContext.hadoopConfiguration.set("dfs.adls.oauth2.client.id", spark.conf.get("fs.adl.oauth2.client.id"))
spark.sparkContext.hadoopConfiguration.set("dfs.adls.oauth2.credential", spark.conf.get("fs.adl.oauth2.credential"))
spark.sparkContext.hadoopConfiguration.set("dfs.adls.oauth2.refresh.url", spark.conf.get("fs.adl.oauth2.refresh.url"))

val readDirectory = dataLakeURL + dataLakeDirectory
val readFile = readDirectory + dataLakeFile
val df = spark.read.json(readFile)


# importing os module  
import os 
  
# importing shutil module  
import shutil 
  
#Source path 
#source = "/home/User/Documents/file.txt"
  
# Destination path 
destination = "/ApplicationData/Essbase/Validation/ShipTo/ResultSets/AllCombinedUsingPythonScript.json"
filenames = [ 'C:/Users/purnima.yadav/Documents/PY/vALIDATIONS/UPload/ShipToBaseDiscrepancy.json',
             'C:/Users/purnima.yadav/Documents/PY/vALIDATIONS/UPload/ShipToBaseDuplicates.json'
            ]
             #'/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseDiscrepancy.json',
 #'/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseDuplicates.json',
 #'/ApplicationData/Essbase/Validation/ShipTo/ResultSets/ShipToBaseOrphan.json'
     #]       

with open('AllCombinedUsingPythonScript.json', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
				