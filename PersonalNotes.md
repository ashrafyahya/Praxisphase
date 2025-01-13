# Eigene Notizen:

## Hardware-Zugangsdaten
- **Benutzername:** `ashraf`
- **Passwort:** `Ashraf123*`
-


git config --global user.name ashrafyahya
git config --global user.email ashrafsadiq97@gmail.com


vscode installation
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg

sudo apt install apt-transport-https
sudo apt update
sudo apt install code # or code-insiders
Quelle:  https://code.visualstudio.com/docs/setup/linux


lsblk
sudo umount /dev/sdX1
sudo dd if=/path/to/image.img of=/dev/sdX bs=4M status=progress
sudo mount /dev/sdX1 /mnt


sudo mkfs.ext4 /dev/mmcblk0p1  # Löschen Für ext4-Format

sudo apt install unzip
unzip ~/Downloads/jetson_orin_nano_image.zip -d ~/Downloads


sudo apt update
sudo apt install gparted
sudo gparted


hostnamectl

sudo usermod -aG sudo ashraf
sudo usermod -aG wheel ashraf

Jetson PINs 
https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/hardware_spec.html

BildQuelle
https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/index.html

VDD_IN Main power – Supplies PMIC and other registers


#nvcc steht für NVIDIA CUDA Compiler
nvcc --version

sudo apt install nano
nano ~/.bashrc
export PATH=/usr/local/cuda/bin:$PATH #einfügen am ende der datei
source ~/.bashrc

Virtuelle Umgebung erstellen 
apt install python3.10-venv 
python3 -m venv yolov5_envx
source yolov5_env/bin/activate
$ deactivate

torch abfragen
pip show torch

torchvision abfragen
pip show torchvision

install torch 
https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html#benefits
jetpack auswählen
https://developer.download.nvidia.com/compute/redist/jp/
Version auswählen
https://developer.download.nvidia.com/compute/redist/jp/v60/pytorch/

torchversion
pip3 install torchversion #letzte version wird installiert
or
pip install torchvision==0.19.0



welche torchversion zu pytorch passt?
https://github.com/pytorch/vision


intelrealsense problem
https://forums.developer.nvidia.com/t/problem-with-intelrealsense/73964



Ubuntu und NVIDIA-Treiber aktualisieren
sudo apt update && sudo apt upgrade -y

Python-Umgebung sicherstellen
sudo apt install python3 python3-pip python3-venv -y
python3 --version

Virtuelle Umgebung erstellen
python3 -m venv yolov8-env
source yolov8-env/bin/activate

YOLOv8 installieren
pip install ultralytics
yolo --version

esten der YOLOv8-Installation
Lade ein Testbild herunter:
wget https://ultralytics.com/images/zidane.jpg -O test.jpg
Erkenne Objekte im Bild
yolo task=detect mode=predict model=yolov8n.pt source=test.jpg

Optimierung für Jetson (optional)
TensorRT verwenden
Konvertiere das Modell in ein TensorRT-Format für bessere Leistung:
yolo export model=yolov8n.pt format=engine


python3 yolov8_segmentation.py


show kameras
v4l2-ctl --list-devices
lsusb
rs-enumerate-devices
realsense-viewer


yolo predict model=yolov8n.pt source=4
