clear && echo -e "
   \e[3m\e[1;92mWE ARE ANONYMOUS, EXPECT US...\e[1;92m
"
apt update && apt upgrade -y && apt install git python -y

echo "PS1= '\e[3m\[\033[1;30m\]\D{%a-%b-%d-%Y} \e[38;5;214m\@
\[\033[1;91m\]\w
 \[\033[0;34m\][\[\033[0;36m\]\#\[\033[0;34m\]]\[\033[1;92m\] '" >> ~/.bashrc
source ~/.bashrc

rm -rf /data/data/com.termux/files/usr/etc/motd
git clone https://github.com/ghoste9624/anonymous-motd /data/data/com.termux/files/usr/etc/motd
echo "/data/data/com.termux/files/usr/etc/motd/init.sh" >> /data/data/com.termux/files/usr/etc/profile # or .zprofile if using zsh
cd /data/data/com.termux/files/usr/etc/motd/ && chmod +x init.sh && cd $HOME
exit
