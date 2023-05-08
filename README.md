# BackupFiles

This tool find BackupFiles

## Installation
```
git clone https://github.com/rix4uni/BackupFiles.git
cd BackupFiles
pip3 install -r requirements.txt
mkdir -p ~/bin
echo -e "\nalias backupfiles='python3 ~/bin/BackupFiles/backupfiles.py'" >> ~/.bashrc
cd .. && mv BackupFiles ~/bin && source ~/.bashrc
```

## Example usages

Single URL:
```
echo "http://testphp.vulnweb.com" | backupfiles -t 100
```

Multiple URLs:
```
cat urls.txt | backupfiles -t 100
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