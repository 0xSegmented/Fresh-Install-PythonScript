import sys
import time
import platform
import distro
import os

dis = distro.name()
if "Nobara" in dis:
    print("Nobara spotted")
    x = input("Ready to install? Press y :\n")
    if x == "y":
        print("Installing....")
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
        else:
            print("Fault3")
    else:
        print("Fault2")
else:
    print("Fault.")
