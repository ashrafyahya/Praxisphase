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

Operating Requirements
Temp. Range (T J )*: -25°C – 105F°C | Supported Power Input: 5V | Operating Lifetime (24x7): 5 years
Jetson Orin Nano 8GB Modes: 7W | 15W
Jetson Orin Nano 4GB Modes: 7W | 10W
Seite 9 in Datasheet

Yes, for devkit it can be 9-20V as there is a power mux on board to choose supply to module. For custom design, should note the voltage level to Orin nano module should be 4.75-5.25V.
https://forums.developer.nvidia.com/t/battery/278439/3

