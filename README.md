 __      __      ___.  __________                            
/  \    /  \ ____\_ |__\______   \ ____   ____  ____   ____  
\   \/\/   // __ \| __ \|       _// __ \_/ ___\/  _ \ /    \ 
 \        /\  ___/| \_\ \    |   \  ___/\  \__(  <_> )   |  \
  \__/\  /  \___  >___  /____|_  /\___  >\___  >____/|___|  /
       \/       \/    \/       \/     \/     \/           \/ 

WebRecon is a tool for conducting basic automated reconnaissance against websites. Built on the sholders of giants, WebRecon uses multiple tools to conduct subdomain enumeration, web host identification, directory enumeration/bruteforcing, port scanning, potential exploit identification, and identification of potentially interesting information.

A big thanks is owed to @tomnomnom, @Fyodor, @offensive-security, and @michenriksen for creating the underlying tools that make this piece of autmation useful.

# Requirements

The following languages and tools are required to run WebRecon.

Languages:
  Go
  Python => 2.7

Tools:
  Nmap            https://nmap.org/download.html
  assetfinder     https://github.com/tomnomnom/assetfinder
  httprobe        https://github.com/tomnomnom/httprobe
  meg             https://github.com/tomnomnom/meg
  gf              https://github.com/tomnomnom/gf
  searchsploit    https://github.com/offensive-security/exploitdb
  aquatone        https://github.com/michenriksen/aquatone

# Install

In order to install the tools required for WebRecon, please visit the links provided above. To install WebRecon itself, simply follow the below steps:

  1. git clone https://github.com/secw01f/webrecon
  2. cd webrecon
  3. pip install -r requirements.txt
