# BackupFiles

This tool find BackupFiles

## Installation
```
git clone https://github.com/rix4uni/BackupFiles.git
cd BackupFiles
#pip3 install -r requirements.txt
```

## Example usages

Single URL:
```
echo "http://testphp.vulnweb.com" | python3 backupfiles.py
```

Multiple URLs:
```
cat urls.txt | python3 backupfiles.py
```

urls.txt contains:
```
http://testphp.vulnweb.com
```

output:
```
http://testphp.vulnweb.com/testphp.vulnweb.com.db 404
http://testphp.vulnweb.com/testphp.vulnweb.com.sql.bak 404
http://testphp.vulnweb.com/testphp.vulnweb.com.zip.bak 404
http://testphp.vulnweb.com/testphp.vulnweb.com.zip.old 404
http://testphp.vulnweb.com/testphp.vulnweb.com.jar 404
http://testphp.vulnweb.com/testphp.vulnweb.com.bz2 404
http://testphp.vulnweb.com/testphp.vulnweb.com.war 404
http://testphp.vulnweb.com/testphp.vulnweb.com.dll 404
```
