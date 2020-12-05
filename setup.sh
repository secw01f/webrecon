#!/bin/bash -i

sudo apt install python3-pip
sudo pip3 install -r requirements.txt

echo "[ ! ] Installing nmap"
sudo apt-get install nmap
echo "[ + ] Nmap installation complete"

echo "[ ! ] Installing go"
cd ~/Downloads && wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.14.2.linux-amd64.tar.gz

if test -f ~/.bashrc;
then
  echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc
  echo "export PATH=\$PATH:~/go/bin" >> ~/.bashrc
  source ~/.bashrc
fi

if test -f ~/.zshrc;
then
  echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.zshrc
  echo "export PATH=\$PATH:~/go/bin" >> ~/.zshrc
  source ~/.zshrc
fi

cd ~
echo "[ + ] Go installation complete"

echo "[ ! ] Installing assetfinder, httprobe, meg, gf, and aquatone"
go get github.com/tomnomnom/assetfinder
go get github.com/tomnomnom/httprobe
go get github.com/tomnomnom/meg
go get github.com/tomnomnom/gf
go get github.com/michenriksen/aquatone

if test -f ~/.bashrc;
then
  echo "source ~/go/src/github.com/tomnomnom/gf/gf-completion.bash" >> ~/.bashrc
  source ~/.bashrc
fi

if test -f ~/.zshrc;
then
  echo "source ~/go/src/github.com/tomnomnom/gf/gf-completion.bash" >> ~/.zshrc
  source ~/.zshrc
fi

cp -r ~/go/src/github.com/tomnomnom/gf/examples ~/.gf
echo "[ + ] Assetfinder, httprobe, meg, gf, and aquatone installation complete"

echo "[ ! ] Installing AMASS"
sudo apt-get install amass
echo "[ + ] AMASS installation complete"

echo "[ ! ] Installing searchsploit"
sudo apt -y install exploitdb
echo "[ + ] Searchsploit installation complete"

echo "[ + ] All installations complete"
