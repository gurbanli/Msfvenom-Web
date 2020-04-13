 
#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

docker image build -t msfvenom_online:local .
docker container run -d -p 8080:5000 msfvenom_online

echo "Successfully created container. Check 127.0.0.1:8080"
