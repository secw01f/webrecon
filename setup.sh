#!/bin/bash

sudo pip install -r requirements.txt

echo "[ ! ] Installing nmap"
sudo apt-get install nmap
echo "[ + ] Nmap installation complete"

echo "[ ! ] Installing go"
cd ~/Downloads && wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.14.2.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
source ~/.bashrc
cd ~
echo "[ + ] Go installation complete"

echo "[ ! ] Installing assetfinder, httprobe, meg, gf, and aquatone"
go get github.com/tomnomnom/assetfinder
go get github.com/tomnomnom/httprobe
go get github.com/tomnomnom/meg
go get github.com/tomnomnom/gf
go get github.com/michenriksen/aquatone
echo "[ + ] Assetfinder, httprobe, meg, gf, and aquatone installation complete"

echo "[ ! ] Installing searchsploit"
sudo apt -y install exploitdb
echo "[ + ] Searchsploit installation complete"

echo "[ + ] All installations complete"
