#!/bin/bash
sudo screen -S minecraft -X stuff "say Serwer zaraz się wyłączyc uciekaj puki możesz^M"
sleep 10
sudo screen -S minecraft -X stuff "stop^M"
echo "Sever Mincraft Został Wyłączony"
sleep 5
sudo screen -S minecraft -X quit
echo "Screen Zozstał Zamknięty"