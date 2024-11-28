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

