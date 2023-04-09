#!/bin/bas
sudo screen -S minecraft -X stuff "say Serwer jest restartowany UWAGA ZARAZ JEBNIE^M"
sudo screen -S minecraft -X stuff "stop^M"
echo "Sever Minecfrat Zatrzymany"
sleep 10
sudo screen -S minecraft -X quit
echo "Scren Został Usunięty"
sleep 5
cd server/
sudo screen -S minecraft -dmS java -Xmx8G -Xms8G -jar paper-1.19.4-492.jar nogui
echo "Server Minecraft Został Uruchomiony Ponownie"