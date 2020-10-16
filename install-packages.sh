echo Basic Upgrade... && \
sudo apt update && sudo apt upgrade -y  && \
echo Installing VSCode... && \
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && \
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ && \
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' && \
echo Installing common dependencies... && \ 
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common && \
sudo apt update && \
sudo apt install -y code && \
echo Install Git... && \
sudo apt install -y git && \
echo Install Python3 and PIP packages for Debugging Module...
sudo apt install -y python3 && \
sudo apt install -y python3-pip && \
pip3 install pytest memory-profiler && \
echo Install and Setting up Docker... && \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" && \
sudo apt update && \
sudo apt install -y docker-ce && \
sudo systemctl status docker && \
sudo usermod -aG docker ${USER} && \
su - ${USER} && \
id -nG && \
echo Cloning Repository.... && \ 
git clone https://github.com/SVCE-ACM/missing-semester-2020.git
