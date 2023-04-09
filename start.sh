#!/bin/bash
cd server/
sudo screen -S minecraft -dmS java -Xmx8G -Xms8G -jar paper-1.19.4-492.jar nogui
echo "Server Uruchomiony"