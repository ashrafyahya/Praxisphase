# Eigene Notizen:

## Hardware-Zugangsdaten
- **Benutzername:** `ashraf`
- **Passwort:** `Ashraf123*`
-


git config --global user.name "Dein Name"
git config --global user.email "deine.email@example.com"


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
python3 -m venv yolov5_env
source yolov5_env/bin/activate
