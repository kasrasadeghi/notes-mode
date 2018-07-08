sudo apt update && upgrade
sudo apt install build-essential curl git -y
sudo apt install python3 python3-pip

curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
bash nodesource_setup.sh
rm nodesource_setup.sh
sudo apt install nodejs npm -y

git clone https://github.com/kasrasadeghi/notes-mode
cd notes-mode
pip3 install virtualenv

sudo apt install direnv -y
echo 'eval "$(direnv hook bash)"' > ~/.bashrc
. ~/.bashrc
virtualenv venv
direnv allow .

cd client
npm install
cd ..

pip3 install -r requirements.txt

sudo apt install docker.io
bash docker.sh
