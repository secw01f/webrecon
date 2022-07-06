#!/bin/bash -i

sudo apt install python3-pip
sudo pip3 install -r requirements.txt

echo "[ ! ] Installing nmap"
sudo apt-get install nmap
echo "[ + ] Nmap installation complete"

echo "[ ! ] Installing Go"
sudo apt-get install golang-go
echo "[ + ] Go installation complete"

echo "[ ! ] Installing assetfinder, httprobe, meg, gf, and aquatone"
go install github.com/tomnomnom/assetfinder@latest
go install github.com/tomnomnom/httprobe@latest
go install github.com/tomnomnom/meg@latest
go install github.com/tomnomnom/gf@latest
GO111MODULE=off go get github.com/michenriksen/aquatone

if test -f ~/.bashrc;
then
    echo "$(find ~/go/pdk/mod/github.com/tomnomnom/ -name gf-completion.bash)" >> ~/.bashrc
    source ~/.bashrc
fi

if test -f ~/.zshrc;
then

    echo "$(find ~/go/pdk/mod/github.com/tomnomnom/ -name gf-completion.zsh)" >> ~/.zshrc
    source ~/.zshrc
fi

cp -r $(find ~/go/pkg/mod/github.com/tomnomnom/gf* -type d -name examples -print) ~/.gf

echo "[ + ] Assetfinder, httprobe, meg, gf, and aquatone installation complete"

echo "[ ! ] Installing Amass"
sudo apt-get install amass
echo "[ + ] Amass installation complete"

echo "[ ! ] Installing SearchSploit"
sudo apt -y install exploit-db
echo "[ + ] SearchSploit installation complete"

echo "[ + ] All installations complete"
