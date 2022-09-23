import sys
import time
import platform
import distro
import os

string.dis = distro.name()
fed = ['Nobara', 'Fedora', 'Ultramarine', 'Risi', 'Qubes', 'Berry', 'ClearOS', 'FX64', 'Montana', 'Kedora', 'Dormant', 'Amahi', 'VortexBox']
if dis in fed:
    print(f"{dis} spotted")
    x = input("Ready to install? Press y :\n")
    if x == "y":
        print("Installing.... Fedora-based")
        time.sleep(0.5)
        print("Enabling fast-mirror and parralel downloads.")
        os.system('sudo rm -rf /etc/dnf/dnf.conf')
        os.system('sudo curl -s https://download1512.mediafire.com/wt669mgu1zag/xiphnq5wu4y0m7v/dnf.conf -o dnf.conf')
        os.system('sudo mv dnf.conf /etc/dnf')
        print("Updating system...")
        time.sleep(0.2)
        print("This might take a while.")
        os.system('sudo dnf update')
        print("Installing Applications...")
        os.system('sudo dnf install neovim htop vlc kdenlive filezilla ktorrent flameshot neofetch cargo git zsh util-linux-user')
        print("Updating pip..")
        os.system('sudo /usr/bin/python3 -m pip install --upgrade pip')
        print("Installing Lunarvim...")
        os.system('bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh) -y')
        print("Installing dotfiles...")
        os.system('rm -rf ~/.config/lvim')
        os.system('git clone https://github.com/MaliciousXatt/lvim.git')
        os.system('mv lvim ~/.config')
        print("Done.")
        time.sleep(0.5)
        shelltype = int(input("1- Ohmyzsh or 2- Ohmybash?\n"))
        if shelltype == 1:
            print("You chose Ohmyzsh.")
            print("Installing ohmyzsh...")
            os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
            os.system('chsh -s $(which zsh)')
        elif shelltype == 2:
            print("You chose Ohmybash.")
            print("Installing ohmybash...")
            os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
            os.system('chsh -s $(which bash)')
        else:
            print("Fault3")
    else:
        print("Fault2")
elif "Arch" in dis or "Artix" in dis or "Manjaro" or "Endeavour" in dis or "Chakra" in dis or "Arco" in dis or "Parabola" in dis or "Garuda" in dis or "RebornOS" in dis or "Asahi" in dis or "SteamOS" in dis or "Ark" in dis or "LinHES" in dis:
    print(f"{dis} spotted")
    x = input("Ready to install? Press y :\n")
    if x == "y":
        print("Installing....Arch-Based")
        time.sleep(0.5)
        print("Updating system...")
        time.sleep(0.2)
        print("This might take a while.")
        os.system('sudo pacman -Syu')
        os.system('yay -Syu')
        print("Installing Applications...")
        os.system('sudo pacman -S neovim htop vlc kdenlive filezilla ktorrent flameshot neofetch cargo git zsh util-linux-user')
        print("Updating pip..")
        os.system('sudo /usr/bin/python3 -m pip install --upgrade pip')
        print("Installing Lunarvim...")
        os.system('bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh) -y')
        print("Installing dotfiles...")
        os.system('rm -rf ~/.config/lvim')
        os.system('git clone https://github.com/MaliciousXatt/lvim.git')
        os.system('mv lvim ~/.config')
        print("Done.")
        time.sleep(0.5)
        shelltype = int(input("1- Ohmyzsh or 2- Ohmybash?\n"))
        if shelltype == 1:
            print("You chose Ohmyzsh.")
            print("Installing ohmyzsh...")
            os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
            os.system('chsh -s $(which zsh)')
        elif shelltype == 2:
            print("You chose Ohmybash.")
            print("Installing ohmybash...")
            os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
            os.system('chsh -s $(which bash)')
        else:
            print("Fault3")
    else:
        print("Fault2")
elif "Debian" in dis or "Ubuntu" in dis or "Mint" in dis or "Deepin" in dis or "Peppermint" in dis or "Mx Linux" in dis or "AntiX" in dis or "PureOS" in dis or "Kali" in dis or "Parrot" in dis or "Devuan" in dis or "Knoppix" in dis or "AV Linux" in dis or "KDE Neon" in dis or "raspian" in dis or "Pop!_OS" in dis or "Tails" in dis:
    print(f"{dis} spotted")
    x = input("Ready to install? Press y :\n")
    if x == "y":
        print("Installing....Debian-Based")
        time.sleep(0.5)
        print("Updating system...")
        time.sleep(0.2)
        print("This might take a while.")
        os.system('sudo apt update && sudo apt upgrade -y')
        print("Installing Applications...")
        os.system('sudo apt install neovim htop vlc kdenlive filezilla ktorrent flameshot neofetch cargo git zsh util-linux-user')
        print("Updating pip..")
        os.system('sudo /usr/bin/python3 -m pip install --upgrade pip')
        print("Installing Lunarvim...")
        os.system('bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh) -y')
        print("Installing dotfiles...")
        os.system('rm -rf ~/.config/lvim')
        os.system('git clone https://github.com/MaliciousXatt/lvim.git')
        os.system('mv lvim ~/.config')
        print("Done.")
        time.sleep(0.5)
        shelltype = int(input("1- Ohmyzsh or 2- Ohmybash?\n"))
        if shelltype == 1:
            print("You chose Ohmyzsh.")
            print("Installing ohmyzsh...")
            os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
            os.system('chsh -s $(which zsh)')
        elif shelltype == 2:
            print("You chose Ohmybash.")
            print("Installing ohmybash...")
            os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
            os.system('chsh -s $(which bash)')
        else:
            print("Fault3")
    else:
        print("Fault2")
else:
    print("Fault.")
print("Done!, Thank you for using the script. - MaliciousXatt")
print("""
Add the following lines to your ~/.zshrc or ~/.bashrc
alias vi="lvim"
alias nvim="lvim"
alias vim="lvim"
export PATH=/home/(ENTER YOUR USERNAME)/.local/bin:$PATH
export PATH=/home/(ENTER YOUR USERNAME)/.cargo/bin:$PATH
""")
