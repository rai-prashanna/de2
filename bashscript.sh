sudo apt install -y openjdk-8-jre-headless
sudo apt install -y python3-pip
pip install pulsar-client==2.7.1 --user
sudo apt install -y net-tools
sudo apt-get install     ca-certificates     curl     gnupg     lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo apt-get install -y docker-ce=5:20.10.14~3-0~ubuntu-focal docker-ce-cli=5:20.10.14~3-0~ubuntu-focal containerd.io
git config --global user.email "prai931024@gmail.com"
git config --global user.name "prai93"