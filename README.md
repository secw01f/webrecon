```
 __      __      ___.  __________                            
/  \    /  \ ____\_ |__\______   \ ____   ____  ____   ____  
\   \/\/   // __ \| __ \|       _// __ \_/ ___\/  _ \ /    \
 \        /\  ___/| \_\ \    |   \  ___/\  \__(  <_> )   |  \
  \__/\  /  \___  >___  /____|_  /\___  >\___  >____/|___|  /
       \/       \/    \/       \/     \/     \/           \/
```

WebRecon is a tool for conducting basic automated reconnaissance against websites. Built on the shoulders of giants, WebRecon uses multiple tools to conduct passive subdomain enumeration, web host identification, directory enumeration/bruteforcing, port scanning, potential exploit identification, and identification of potentially interesting information.

A big thanks is owed to @tomnomnom, @OWASP, @Fyodor, @offensive-security, and @michenriksen for creating the underlying tools that make this piece of automation useful.

# Requirements

The following languages and tools are required to run WebRecon.

Languages:  
  Go  
  Python => 2.7

Tools:  
  Nmap: https://nmap.org/download.html  
  assetfinder: https://github.com/tomnomnom/assetfinder  
  AMASS: https://github.com/OWASP/Amass  
  httprobe: https://github.com/tomnomnom/httprobe  
  meg: https://github.com/tomnomnom/meg  
  gf: https://github.com/tomnomnom/gf  
  searchsploit: https://github.com/offensive-security/exploitdb  
  aquatone: https://github.com/michenriksen/aquatone  

**(Note)** The nmap scanning completed by WebRecon is low and slow but can be changed by simply editing the arguments in *webrecon/lib/nmapscanner.py*.

# Install

In order to install the tools required for WebRecon, please follow the steps below:

**(Note)** This is only the instructions for installing on Kali Linux. More platforms will be added at a later time.

  1. git clone https://github.com/secw01f/webrecon
  2. cd webrecon
  3. chmod +x setup.sh
  4. ./setup.sh
  5. Open a new terminal
  6. Navigate to your WebRecon installation and run the tool
