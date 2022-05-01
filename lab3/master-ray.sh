
    1  exit
    2  sudo apt update
    3  sudo apt upgrade
    4  sudo apt update
    5  sudo apt upgrade -y
    6  .local/bin/ray start --head --port=6379
    7  python3 -m pip install -U "ray[default]"
    8  sudo apt install -y python3-pip
    9  python3 -m pip install --upgrade pip
   10  python3 -m pip install -U "ray[default]"
   11  .local/bin/ray start --head --port=6379
   12  exit
   13  python3 -m pip install -U jupyter
   14  .local/bin/jupyter notebook
   15  ray stop
   16  .local/bin/jupyter notebook
   17  exit
   18  .local/bin/jupyter notebook
   19  clear
   20  ls
   21  history 
   python3 -m jupyterlab --ip=* --port=8888
